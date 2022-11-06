from urllib import response
from django.conf import settings
from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from jobportal.settings import BASE_DIR
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date
import os

# Create your views here.
def index(request):
    return render(request,'index.html')

def admin_login(request):
    error=""
    if request.method=='POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user=authenticate(username=uname,password=pwd)
        
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    # else:
    #     error = "yes"
    dic = {'error':error}
    return render(request,'admin_login.html',dic)

def candidate_login(request):
    error=""
    if request.method=='POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user=authenticate(username=uname,password=pwd)
        
        try:
            user1 = userdetails.objects.get(user=user)
            if user1.type == "candidate":
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    # else:
    #     error = "yes"
    dic = {'error':error}
    return render(request,'candidate_login.html',dic)

def candidate_sign_up(request):
    error=""
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        # d = request.POST['dob']
        g = request.POST['gender']
        mob = request.POST['mobile']
        e = request.POST['email']
        p = request.POST['pwd']
        try:
        #    uname=f+str(mob[-2:])
           user= User.objects.create_user(first_name=f,last_name=l,username=e,password=p,email=e)
           userdetails.objects.create(user=user,mobile=mob,gender=g,type="candidate")
           error="no"
        except:
            error="yes"
    dic = {'error': error}
    return render(request,'candidate_sign_up.html',dic)


def recruiter_login(request):
    error=""
    if request.method=='POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user=authenticate(username=uname,password=pwd)
        
        try:
            user1 = recruiter_details.objects.get(user=user)
            if user1.type == "recruiter" and user1.status!="pending":
                login(request,user)
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    # else:
    #     error = "yes"
    dic = {'error':error}
    return render(request,'recruiter_login.html',dic)


def recruiter_signup(request):
    error=""
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        mob = request.POST['mobile']
        e = request.POST['email']
        c = request.POST['company']
        p = request.POST['pwd']
        try:
        #    uname=f+str(mob[-2:])
           user= User.objects.create_user(first_name=f,last_name=l,username=e,password=p,email=e)
           recruiter_details.objects.create(user=user,mobile=mob,company=c,type="recruiter",status="pending")
           error="no"
        except:
            error="yes"
    dic = {'error': error}
    return render(request,'recruiter_signup.html',dic)


def Logout(request):
    logout(request)
    return redirect('index')


def candidate_home(request):
    if not request.user.is_authenticated:
        return redirect('candidate_login')
    
    user1 = request.user
    candidate = userdetails.objects.get(user=user1)
    
    error=""
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        mob = request.POST['mobile']
        g = request.POST['gender']

        candidate.user.first_name=f
        candidate.user.last_name=l
        candidate.mobile=mob
        candidate.gender=g
        try:
            candidate.save()
            candidate.user.save()
            error="no"
        except:
            error="yes"
    d = {'candidate':candidate,'error': error}
    return render(request,'candidate_home.html',d)

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    
    user1 = request.user
    recruiter = recruiter_details.objects.get(user=user1)
    
    error=""
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        mob = request.POST['mobile']

        recruiter.user.first_name=f
        recruiter.user.last_name=l
        recruiter.mobile=mob
        try:
            recruiter.save()
            recruiter.user.save()
            error="no"
        except:
            error="yes"
    d = {'recruiter':recruiter,'error': error}
    return render(request,'recruiter_home.html',d)

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    rcount= recruiter_details.objects.all().count()
    ccount= userdetails.objects.all().count()
    d = {'rcount':rcount, 'ccount':ccount}
    return render(request,'admin_home.html',d)

def view_candidates(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = userdetails.objects.all()
    dic = {'data': data}
    return render(request,'view_candidates.html',dic)


def delete_candidate(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    candidate = User.objects.get(id=pid)
    candidate.delete()
    return redirect('view_candidates')

def pendingrequests(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = recruiter_details.objects.filter(status='pending')
    dic = {'data': data}
    return render(request,'pendingrequests.html',dic)

def approve(request,rid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = recruiter_details.objects.get(id=rid)
    data.status = "approved"
    data.save()
    return redirect('pendingrequests')

def reject(request,rid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = User.objects.get(id=rid)
    data.delete()
    return redirect('pendingrequests')

def view_recruiters(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = recruiter_details.objects.all()
    dic = {'data': data}
    return render(request,'view_recruiters.html',dic)


def change_pass_admin(request):
    error=""
    if request.method=='POST':
        c = request.POST['pwd']
        p = request.POST['cnpwd']
        try:
            user= User.objects.get(id=request.user.id)
            if user.check_password(c):
                user.set_password(p)
                user.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    dic = {'error': error}
    return render(request,'change_pass_admin.html',dic)


def change_pass_candidate(request):
    error=""
    if request.method=='POST':
        c = request.POST['pwd']
        p = request.POST['cnpwd']
        try:
            user= User.objects.get(id=request.user.id)
            if user.check_password(c):
                user.set_password(p)
                user.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    dic = {'error': error}
    return render(request,'change_pass_candidate.html',dic)



def change_pass_recruiter(request):
    error=""
    if request.method=='POST':
        c = request.POST['pwd']
        p = request.POST['cnpwd']
        try:
            user= User.objects.get(id=request.user.id)
            if user.check_password(c):
                user.set_password(p)
                user.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    dic = {'error': error}
    return render(request,'change_pass_recruiter.html',dic)



def post_jobs(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=""
    if request.method=='POST':
        t = request.POST['title']
        loc = request.POST['location']
        s = request.POST['salary']
        e = request.POST['end_date']
        exp = request.POST['experience']
        skill = request.POST['skills']
        des = request.POST['description']
        
        
        user1=request.user
        recruiter1=recruiter_details.objects.get(user=user1)
        try:
           jobs.objects.create(recruiter=recruiter1,end_date=e,title=t,salary=s,location=loc,experience=exp,skills=skill,description=des,company=recruiter1.company)
           error="no"
        except:
            error="yes"
    dic = {'error': error}
    return render(request,'post_jobs.html',dic)



def job_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user1=request.user
    recruiter1=recruiter_details.objects.get(user=user1)
    data = jobs.objects.filter(recruiter=recruiter1)
    dic = {'data':data}
    return render(request,'job_list.html',dic)


def job_list_candidate(request):
    if not request.user.is_authenticated:
        return redirect('candidate_login')
    
    user1=request.user
    candidate1=userdetails.objects.get(user=user1)
    job = jobs.objects.all()
    data=applied.objects.filter(candidate=candidate1)
    
    li = []
    for i in data:
        li.append(i.job.id)
        
    dic = {'job':job,'li':li}
    return render(request,'job_list_candidate.html',dic)

def latest_jobs(request):
    data = jobs.objects.all().order_by('end_date')
    dic = {'data':data}
    return render(request,'latest_jobs.html',dic)


def delete_job(request,rid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    data = jobs.objects.get(id=rid)
    data.delete()
    return redirect('job_list')


def edit_job(request,jid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=""
    job=jobs.objects.get(id=jid)
    if request.method=='POST':
        t = request.POST['title']
        loc = request.POST['location']
        s = request.POST['salary']
        e = request.POST['end_date']
        exp = request.POST['experience']
        skill = request.POST['skills']
        des = request.POST['description']
        
        job.title=t
        job.location=loc
        job.salary=s
        job.experience=exp
        job.skills=skill
        job.description=des
        
        try:
            job.save()
            error="no"
        except:
            error="yes"
        
        if e:
            job.end_date=e
            job.save()
        
    dic = {'error': error,'job':job}
    return render(request,'edit_job.html',dic)

def job_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect('candidate_login')
    data = jobs.objects.get(id=pid)
    d = {'job':data}
    return render(request,'job_detail.html',d)

def apply_for_job(request,pid):
    if not request.user.is_authenticated:
        return redirect('candidate_login')
    
    error=""
    user1 = request.user
    candidate = userdetails.objects.get(user=user1)
    job = jobs.objects.get(id=pid)
    
    date1 = date.today()
    if job.end_date < date1:
        error="close"
    else:
        if request.method == 'POST':
            r = request.FILES['resume']
            applied.objects.create(resume=r,applied_date=date1,candidate=candidate,job=job)
            error="ok"
    d = {'error':error,'candidate':candidate}
    return render(request,'apply_for_job.html',d)


def applied_candidates(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    
    data = applied.objects.all()
    dic = {'data':data}
    return render(request,'applied_candidates.html',dic)

