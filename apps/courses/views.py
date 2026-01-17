from django.shortcuts import render

# Create your views here.


def course_list(request):
    courses = [
        {
            'id': 1,
            'level': 'Principiante',
            'rating': 4.8,
            'course_title': 'Python: fundamentos hasta los detalles',
            'instructor': 'Alison Walsh',
            'course_image': 'images/curso_1.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/68.jpg',
        },
        {
            'id': 2,
            'level': 'Intermedio',
            'rating': 4.9,
            'course_title': 'Django: crea aplicaciones Robustas',
            'instructor': 'Patty Kutch',
            'course_image': 'images/curso_2.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/20.jpg',
        },
        {
            'id': 3,
            'level': 'Avanzado',
            'rating': 4.8,
            'course_title': 'Django Advanced Level Course',
            'instructor': 'Alonzo Murray',
            'course_image': 'images/curso_3.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/32.jpg',
        },
        {
            'id': 4,
            'level': 'Avanzado',
            'rating': 4.8,
            'course_title': 'FastApi: Building APIs with Python and FastAPI',
            'instructor': 'Gregory Harris',
            'course_image': 'images/curso_4.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/45.jpg',
        },
    ]
    
    return render(request, 'courses/courses.html', {'courses': courses})

def course_detail(request):
    return render(request, 'courses/course_detail.html')

def course_lessons(request):
    return render(request, 'courses/course_lessons.html')
