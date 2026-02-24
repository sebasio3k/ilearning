from django.urls import path
from ..views import instructor

app_name = 'instructor'

urlpatterns = [
    path('courses/', instructor.CourseListView.as_view(), name='course_list'),
    path('course/create/', instructor.CourseCreateView.as_view(), name='course_create'),
    path('course/<int:pk>/edit/', instructor.CourseUpdateView.as_view(), name='course_edit'),
    path('course/<int:pk>/delete/', instructor.CourseDeleteView.as_view(), name='course_delete'),
    # Modules Urls
    path('course/<int:course_pk>/modules/', instructor.ModuleListView.as_view(), name='module_list'),
    path('course/<int:course_pk>/modules/add', instructor.ModuleCreateView.as_view(), name='module_create'),
    path('modules/<int:pk>/edit', instructor.ModuleUpdateView.as_view(), name='module_edit'),
    path('modules/<int:pk>/delete', instructor.ModuleDeleteView.as_view(), name='module_delete'),
    # Content urls
    path('module/<int:module_pk>/contents', instructor.ContentListView.as_view(), name='content_list'),
    path('module/<int:module_pk>/content/<model_name>/add', instructor.ContentCreateUpdateView.as_view(), name='content_create'),
    path('module/<int:module_pk>/content/<int:pk>/<model_name>/edit', instructor.ContentCreateUpdateView.as_view(), name='content_edit'),
]