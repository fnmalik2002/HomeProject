from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('payments/', views.payments, name='payments'),
    path('reset/', views.reset_password, name='reset'),
    path('mark_done/', views.mark_done, name='mark_done'),
    path('review_done/', views.review_done, name='review_done'),
    path('mark_not_done/', views.mark_done, name='mark_not_done'),
    path('dashboard/', views.dashboard, name='dashboard'),
]