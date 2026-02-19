from django.urls import path
from .views import (
    homepage,
    presentations_list,
    casestudy_list,
    listening_list,
    independent_list,
    assignments_list,
    quiz_list,
    about,
    courses
)

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', homepage, name='homepage'),

    path('presentations/', presentations_list, name='presentations'),
    path('casestudy/', casestudy_list, name='casestudy'),
    path('listening/', listening_list, name='listening'),
    path('independent/', independent_list, name='independent'),
    path('assignments/', assignments_list, name='assignments'),
    path('quiz/', quiz_list, name='quiz'),
    path('about/', about, name='about'),
    path('courses/', courses, name='courses'),
    path("create-admin/", create_admin),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])