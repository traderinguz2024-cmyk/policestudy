from django.urls import path
from .views import *


from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.all_categories),
    path('category/<str:type>/<int:pk>/', views.category_detail),
    path('start-test/', views.start_test),
    path('check-test/', views.check_test),
]


