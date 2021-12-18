from django.http import HttpResponseRedirect, HttpResponse
# from django.http.request import HttpRequest
from django.template import loader
from django.shortcuts import render, get_object_or_404
# from django.urls import reverse
# from django.views import generic
from .models import JobPost, Payments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    
    

    print(request.user)
    find_record = User.objects.get(username = request.user)
    user_id = find_record.id
    if request.user.is_superuser:
        
        job_list = JobPost.objects.filter(job_taken= False).order_by('-id')[:10] 
        job_gone = JobPost.objects.filter(job_taken= True).order_by('-id')[:10]
    else:

        job_list = JobPost.objects.filter(job_taker = user_id).order_by('-id')[:10] 
        job_gone = JobPost.objects.filter(job_taken= True).order_by('-id')[:10]

    template = loader.get_template('jobs/index.html')
    context = {
    'job_list': job_list,
     'job_gone' : job_gone,
     }
    return HttpResponse(template.render(context, request))


@login_required
def detail(request, pk):
    print(pk)
    detail = get_object_or_404(JobPost, pk=pk) 
    template = loader.get_template('jobs/detail.html')
    context = {
    'detail': detail, }
    return HttpResponse(template.render(context, request))

def payments(request):
    
    find_record = User.objects.get(username = request.user)
    user_id = find_record.id
    print(request.user, user_id)
    # if request.user.is_superuser:       
    #     job_list = JobPost.objects.filter(job_taken= False).order_by('-id')[:10] 
    #     job_gone = JobPost.objects.filter(job_taken= True).order_by('-id')[:10]
    # else:
    #     job_list = JobPost.objects.filter(job_taker = user_id).order_by('-id')[:10] 
    #     job_gone = JobPost.objects.filter(job_taken= True).order_by('-id')[:10]

    pk=request.POST['Choice']
    print("choice id : ", pk)
    upd_rec = JobPost.objects.get(pk=pk)
    upd_rec.job_taken = True
    # upd_rec.job_taker = user_id
    upd_rec.save()
    
    
    payment_list = JobPost.objects.filter(job_taken= True).order_by('-id')[:5] 
    template = loader.get_template('jobs/payments.html')
    context = {
    'payment_list': payment_list,
    'user': request.user,
     }
    return HttpResponse(template.render(context, request))

