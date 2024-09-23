

from django.urls import path # type: ignore
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
]

