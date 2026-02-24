from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from ..models import Course, Module, Content, Text, File, Image, Video
from django.shortcuts import get_object_or_404, redirect, render
from django.forms import modelform_factory
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseForbidden

CONTENT_MODELS= {
    'text': Text,
    'file': File,
    'image': Image,
    'video': Video
}

class InstructorRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        return self.request.user.is_instructor
    
class CourseListView(InstructorRequiredMixin, ListView):
    model = Course
    template_name = 'instructor/course_list.html'
    context_object_name = 'courses'
    paginate_by = 8
    
    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)
    
class CourseCreateView(InstructorRequiredMixin, CreateView):
    model = Course
    fields = ['title', 'overview', 'image', 'level', 'duration', 'categories', 'slug', 'duration']
    template_name = 'instructor/course_form.html'
    success_url = reverse_lazy('instructor:course_list')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CourseUpdateView(InstructorRequiredMixin, UpdateView):
    model = Course
    fields = ['title', 'overview', 'image', 'level', 'duration', 'categories', 'slug', 'duration']
    template_name = 'instructor/course_form.html'
    success_url = reverse_lazy('instructor:course_list')
    
    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)

class CourseDeleteView(InstructorRequiredMixin, DeleteView):
    model = Course
    template_name = 'instructor/course_confirm_delete.html'
    success_url = reverse_lazy('instructor:course_list')
    
    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)
    

# Module views
class ModuleListView(InstructorRequiredMixin, ListView):
    model = Module
    template_name = 'instructor/module_list.html'
    context_object_name = 'modules'
    
    def get_queryset(self):
        self.course = get_object_or_404(
            Course, 
            pk=self.kwargs['course_pk'], 
            owner=self.request.user
        )
        return self.course.modules.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.course
        return context
    
class ModuleCreateView(InstructorRequiredMixin, CreateView):
    model = Module
    fields = ['title', 'description']
    template_name = 'instructor/module_form.html'
    
    def get_success_url(self):
        return reverse('instructor:module_list', args=[self.kwargs['course_pk']])
    
    def form_valid(self, form):
        form.instance.course = get_object_or_404(
            Course, 
            pk=self.kwargs['course_pk'], 
            owner=self.request.user
        )
        return super().form_valid(form)
    
class ModuleUpdateView(InstructorRequiredMixin, UpdateView):
    model = Module
    fields = ['title', 'description']
    template_name = 'instructor/module_form.html'
    
    def get_success_url(self):
        return reverse('instructor:module_list', args=[self.object.course.pk])
    
    def get_queryset(self):
        return Module.objects.filter(course__owner=self.request.user)
    
class ModuleDeleteView(InstructorRequiredMixin, DeleteView):
    model = Module
    template_name = 'instructor/module_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('instructor:module_list', args=[self.object.course.pk])
    
    def get_queryset(self):
        return Module.objects.filter(course__owner=self.request.user)
    
# Content views
class ContentListView(InstructorRequiredMixin, ListView):
    model = Content
    template_name = 'instructor/content_list.html'
    context_object_name = 'contents'
    
    def get_queryset(self):
        self.module = get_object_or_404(
            Module, 
            pk=self.kwargs['module_pk'], 
            course__owner=self.request.user
        )
        return self.module.contents.all().select_related('content_type').order_by('order')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module'] = self.module
        return context

class ContentCreateUpdateView(InstructorRequiredMixin, View):
    template_name = 'instructor/content_form.html'
    
    def get_model(self, model_name):
        return CONTENT_MODELS.get(model_name, None)
    
    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(model, exclude=['owner', 'created_at', 'updated_at'])
        return Form(*args, **kwargs)

    def dispatch(self, request, module_pk=None, model_name=None, pk=None, *args, **kwargs):
        self.module = get_object_or_404(
            Module, 
            pk=module_pk, 
            course__owner=request.user
        )
        self.model = self.get_model(model_name)
        self.object = None
        
        if pk:
            try:
                content = Content.objects.select_related('content_type').get(
                    object_id=pk,
                    content_type=ContentType.objects.get_for_model(self.model),
                    module=self.module
                )
                self.object = content.item
            except Content.DoesNotExist:
                return HttpResponseForbidden('Dont have permission to edit this content, or content does not exist')
        
        return super().dispatch(request, module_pk, model_name, pk, *args, **kwargs)    

    def get(self, request, module_pk, model_name, pk=None):
        form = self.get_form(self.model, instance=self.object)
        return render(request, self.template_name, {'form': form, 'object': self.object})
    
    def post(self, request, module_pk, model_name, pk=None):
        form = self.get_form(self.model, data=request.POST, files=request.FILES, instance=self.object)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            if not pk:
                Content.objects.create(
                    module=self.module,
                    item=obj
                )
            return redirect('instructor:content_list', module_pk=self.module.pk)
        return render(request, self.template_name, {'form': form, 'object': self.object})

class ContentDeleteView(InstructorRequiredMixin, DeleteView):
    model = Content
    template_name = 'instructor/content_confirm_delete.html'
    
    def get_queryset(self):
        return Content.objects.filter(module__course__owner=self.request.user)
    
    def get_success_url(self):
        return reverse('instructor:content_list', args=[self.object.module.pk])