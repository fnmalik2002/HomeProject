from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('payments/', views.payments, name='payments'),
    path('reset/', views.reset_password, name='reset'),
    path('register/', views.register, name='register'),
    path('register/', views.register, name='add_user'),
    path('mark_done/', views.mark_done, name='mark_done'),
    path('review_done/', views.review_done, name='review_done'),
    path('mark_not_done/', views.mark_done, name='mark_not_done'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('new_job/', views.new_job, name='new_job'),
    path('<int:pk>/repost_job/', views.repost_job, name='repost_job'),
    path('job_payments/', views.job_payments, name='job_payments'),
]