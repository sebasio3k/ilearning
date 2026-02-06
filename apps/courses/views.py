from django.shortcuts import render
from .models import Course

# Create your views here.


def course_list(request):
    courses = Course.objects.all()
    # courses = [
    #     {
    #         'id': 1,
    #         'level': 'Principiante',
    #         'rating': 4.8,
    #         'course_title': 'Python: fundamentos hasta los detalles',
    #         'instructor': 'Alison Walsh',
    #         'course_image': 'images/curso_1.jpg',
    #         'instructor_image': 'https://randomuser.me/api/portraits/women/68.jpg',
    #     },
    #     {
    #         'id': 2,
    #         'level': 'Intermedio',
    #         'rating': 4.9,
    #         'course_title': 'Django: crea aplicaciones Robustas',
    #         'instructor': 'Patty Kutch',
    #         'course_image': 'images/curso_2.jpg',
    #         'instructor_image': 'https://randomuser.me/api/portraits/women/20.jpg',
    #     },
    #     {
    #         'id': 3,
    #         'level': 'Avanzado',
    #         'rating': 4.8,
    #         'course_title': 'Django Advanced Level Course',
    #         'instructor': 'Alonzo Murray',
    #         'course_image': 'images/curso_3.jpg',
    #         'instructor_image': 'https://randomuser.me/api/portraits/men/32.jpg',
    #     },
    #     {
    #         'id': 4,
    #         'level': 'Avanzado',
    #         'rating': 4.8,
    #         'course_title': 'FastApi: Building APIs with Python and FastAPI',
    #         'instructor': 'Gregory Harris',
    #         'course_image': 'images/curso_4.jpg',
    #         'instructor_image': 'https://randomuser.me/api/portraits/men/45.jpg',
    #     },
    # ]
    
    return render(request, 'courses/courses.html', {'courses': courses})

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
