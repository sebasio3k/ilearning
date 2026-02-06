import logging
from django.shortcuts import render
from .models import Course
from django.db.models import Q

# Create your views here.
logger = logging.getLogger(__name__)


def course_list(request):
    courses = Course.objects.all()
    
    query = request.GET.get('query').strip()
    if query:
        logger.info(f"Buscando cursos con el query: {query}")
        courses = courses.filter(
            Q(title__icontains=query) | 
            Q(owner__first_name__icontains=query) |
            Q(owner__last_name__icontains=query)
        )
    
    return render(request, 'courses/courses.html', {'courses': courses, 'query': query})

def course_detail(request):
    course = {
        'course_title': 'Python: fundamentos hasta los detalles',
        'course_link': 'course_lessons',
        'course_image': 'images/curso_2.jpg',
        'info_course': {
            'lessons': 79,
            'duration': 8,
            'instructor': 'Alison Walsh',
        },
        'course_content': [
            {
                'id': 1,
                'name': 'Introducción al curso',
                'lessons': [
                    {
                        'name': '¿Qué aprenderás en este curso?',
                        'type': 'video',
                    },
                    {
                        'name': 'Cóm usar la plataforma',
                        'type': 'article',
                    },
                ]
            },
        ]
    }
    return render(request, 'courses/course_detail.html', {'course': course})

def course_lessons(request):
    lessons = {
        'course_title': 'Django: Crea aplicaciones web robustas con Python',
        'progress': 30,
        'course_content': [
            {
                'id': 1,
                'name': 'Introducción al curso',
                'total_lessons': 6,
                'completed_lessons': 2,
                'lessons': [
                    {
                        'name': '¿Qué aprenderás en este curso?',
                        'type': 'video',
                    },
                    {
                        'name': 'Cóm usar la plataforma',
                        'type': 'article',
                    },
                ]
            },
            {
                'id': 2,
                'name': 'Fundamentos necesarios de Python',
                'total_lessons': 27,
                'completed_lessons': 0,
                'lessons': [
                    {
                        'name': 'Variables',
                        'type': 'video',
                    },
                    {
                        'name': 'Condicionales',
                        'type': 'video',
                    },
                ]
            },
        ]
    }
    return render(request, 'courses/course_lessons.html', {'lessons': lessons})
