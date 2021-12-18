from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('payments/', views.payments, name='payments'),
]