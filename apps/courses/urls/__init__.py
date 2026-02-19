from .instructor import urlpatterns as instructor_urls
# from .student import urlpatterns as student_urls

urlpatterns = [
    *instructor_urls,
    # *student_urls
]