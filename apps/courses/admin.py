from django.contrib import admin
from .models import Course, Category, CourseCategory, Module, Enrollment, Progress, Review, Content, Text, File, Image, Video


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['course', 'category']
    list_filter = ['category']
    search_fields = ['course__title']


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    list_filter = ('title', 'course__title')


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at')
    list_filter = ('course', 'enrolled_at')
    search_fields = ['user__username', 'course__title']


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'progress', 'status', 'updated_at')
    list_filter = ('status',)
    search_fields = ['user__username', 'course__title']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ['user__username', 'course__title', 'comment', 'rating']


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('module', 'content_type', 'item')
    list_filter = ('module',)


@admin.register(Text)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'updated_at', 'content')


@admin.register(File)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'updated_at', 'file')


@admin.register(Video)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'updated_at', 'url')


@admin.register(Image)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'updated_at', 'image')

