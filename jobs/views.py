from django.http import HttpResponseRedirect, HttpResponse
# from django.http.request import HttpRequest
from django.template import loader
from django.shortcuts import render, get_object_or_404
# from django.urls import reverse
# from django.views import generic
from .models import JobPost, Payments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.utils import timezone
from django.db.models import Avg, Count, Min, Sum

# Create your views here.
@login_required
def index(request):
    print("user type : ",type(request.user))
    user = User.objects.get(username = request.user)
    user_group = Group.objects.get(user = request.user)
    print('user_group', user_group)
    
    users_in_a_group = User.objects.filter(groups=user_group)
    def job_creator(users_in_a_group):
        for u in users_in_a_group:
            job_list_1 = JobPost.objects.filter(job_creator = u).order_by('-id')[:10] 
            print(type(u), u, job_list_1, len(job_list_1))
            if len(job_list_1) > 0:
                print("job creator is", u)
                return u
    
    

    
    this_family_jobs = JobPost.objects.filter(job_creator=job_creator(users_in_a_group))

    # print('this_family_jobs : ', this_family_jobs)
    
    if request.user.is_superuser:
        
        job_list = this_family_jobs.filter(job_taken= False).order_by('-id')[:10] 
        job_gone = this_family_jobs.filter(job_taken= True).order_by('-id')[:10]
        my_unfinished_jobs = this_family_jobs.filter(job_taker=user).filter(job_taken=True).filter(job_done=False).order_by('-id')[:10]
        my_done_jobs = this_family_jobs.filter(job_taker=user).filter(job_done=True).order_by('-id')[:10]
        my_money_under_review_this_month = this_family_jobs.filter(job_taker=user).filter(job_taken=True).filter(job_done=False).aggregate(Sum('job_price'))
        my_total_this_mont = this_family_jobs.filter(job_taker=user).filter(job_taken=True).filter(job_done=True).aggregate(Sum('job_price'))
        unclaimed = this_family_jobs.filter(job_taken= False).aggregate(Sum('job_price'))

    else:

        job_list = this_family_jobs.filter(job_taken= False).order_by('-id')[:10]  
        job_gone = this_family_jobs.filter(job_taken= True).order_by('-id')[:10]
        my_unfinished_jobs = this_family_jobs.filter(job_taker=user).filter(job_taken=True).filter(job_done=False).order_by('-id')[:10]
        my_done_jobs = this_family_jobs.filter(job_taker=user).filter(job_done=True).order_by('-id')[:10]
        my_money_under_review_this_month = this_family_jobs.filter(job_taker=user).filter(job_taken=True).filter(job_done=False).aggregate(Sum('job_price'))
        my_total_this_mont = this_family_jobs.filter(job_taker=user).filter(job_taken=True).filter(job_done=True).aggregate(Sum('job_price'))
        unclaimed = this_family_jobs.filter(job_taken= False).aggregate(Sum('job_price'))
    
    
    template = loader.get_template('jobs/index.html')
    print("Money", my_money_under_review_this_month)
    
    if request.user == 'AnonymousUser':
        usr = "None"
    else:
        usr = request.user
    context = {
    'job_list': job_list,
     'job_gone' : job_gone,
     'my_unfinished_jobs' : my_unfinished_jobs,
     'my_done_jobs' : my_done_jobs,
     'user': usr,
     'my_money_under_review_this_month':my_money_under_review_this_month,
     'my_total_this_mont': my_total_this_mont,
     'unclaimed':unclaimed,
     }
    return HttpResponse(template.render(context, request))


@login_required
def detail(request, pk):
    print(pk)
    detail = get_object_or_404(JobPost, pk=pk) 
    template = loader.get_template('jobs/detail.html')
    if request.user == 'AnonymousUser':
        usr = "None"
    else:
        usr = request.user
    context = {
    'detail': detail,
    'user': usr, }
    return HttpResponse(template.render(context, request))

def payments(request):
    
    user = User.objects.get(username = request.user)
    
    print(request.user, user.id)
    # if request.user.is_superuser:       
    #     job_list = JobPost.objects.filter(job_taken= False).order_by('-id')[:10] 
    #     job_gone = JobPost.objects.filter(job_taken= True).order_by('-id')[:10]
    # else:
    #     job_list = JobPost.objects.filter(job_taker = user_id).order_by('-id')[:10] 
    #     job_gone = JobPost.objects.filter(job_taken= True).order_by('-id')[:10]
    try:
        pk=request.POST['Choice']
        print("choice id : ", pk)
        upd_rec = JobPost.objects.get(pk=pk)
        upd_rec.job_taken = True
        upd_rec.job_taker = user
        upd_rec.save()
    except Exception as e:
        print(e)
        
    payment_list = JobPost.objects.filter(job_taken= True).filter(job_done= False).order_by('-id')[:10] 
    template = loader.get_template('jobs/payments.html')
    if request.user == 'AnonymousUser':
        usr = "None"
    else:
        usr = request.user
    context = {
    'payment_list': payment_list,
    'user': usr,
     }
    # return HttpResponse(template.render(context, request))
    return index(request)

def reset_password(request): 
    template = loader.get_template('registration/reset.html')
    context = { 
    'user': request.user,
     }
    return HttpResponse(template.render(context, request))

def mark_done(request):
    pk=request.POST['Choice']
    print("choice id : ", pk)
    print(type(pk))
    if int(pk) > 0:
        upd_rec = JobPost.objects.get(pk=pk)
        upd_rec.job_done = True
        upd_rec.job_done_date = timezone.now()
        upd_rec.save()  
    elif int(pk) < 0:
        pkid = str(-1*int(pk))
        print(type(pkid), pkid, "else statement")
        
        try:
            upd_rec = JobPost.objects.get(pk=pkid)
            upd_rec.job_taken = False
            
            upd_rec.job_taker = User.objects.get(username = 'nouser')
            upd_rec.save()
        except Exception as e:
            print(e)
            print('exception happened')
    elif int(pk)==0:
        try:
            jobss = JobPost.objects.all()
            print(jobss)
            for job in jobss:
                print(job)
                job.job_taken = False
                job.job_done = False
                job.job_done_date = None
                job.job_taker = User.objects.get(username = 'nouser')
                job.save()
        except Exception as e:
            print(e)
            print('exception happened')
        

    return index(request)
def mark_not_done(request):
    print("Not done selected")
    return index(request)


    
