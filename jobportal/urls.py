"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from job_portal.views import *
from django.conf.urls.static import static
from django.urls import path

from django.views.static import serve
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('latest_jobs',latest_jobs,name="latest_jobs"),
    path('admin_login',admin_login,name="admin_login"),
    path('candidate_login',candidate_login,name="candidate_login"),
    path('recruiter_login',recruiter_login,name="recruiter_login"),
    path('candidate_sign_up',candidate_sign_up,name="candidate_sign_up"),
    path('recruiter_signup',recruiter_signup,name="recruiter_signup"),
    path('candidate_home',candidate_home,name="candidate_home"),
    path('candidate_update',candidate_update,name="candidate_update"),
    path('recruiter_home',recruiter_home,name="recruiter_home"),
    path('recruiter_update',recruiter_update,name="recruiter_update"),
    path('admin_home',admin_home,name="admin_home"),
    path('view_candidates',view_candidates,name="view_candidates"),
    path('view_recruiters',view_recruiters,name="view_recruiters"),
    path('delete_candidate/<int:pid>',delete_candidate,name="delete_candidate"),
    path('pendingrequests',pendingrequests,name="pendingrequests"),
    path('approve/<int:rid>',approve,name="approve"),
    path('reject/<int:rid>',reject,name="reject"),
    path('change_pass_admin',change_pass_admin,name="change_pass_admin"),
    path('change_pass_candidate',change_pass_candidate,name="change_pass_candidate"),
    path('change_pass_recruiter',change_pass_recruiter,name="change_pass_recruiter"),
    path('post_jobs',post_jobs,name="post_jobs"),
    path('job_list',job_list,name="job_list"),
    path('job_list_candidate',job_list_candidate,name="job_list_candidate"),
    path('delete_job/<int:rid>',delete_job,name="delete_job"),
    path('edit_job/<int:jid>',edit_job,name="edit_job"),
    path('job_detail/<int:pid>',job_detail,name="job_detail"),
    path('apply_for_job/<int:pid>',apply_for_job,name="apply_for_job"),
    path('applied_candidates',applied_candidates,name="applied_candidates"),
    path('reject_candidate/<int:xid>',reject_candidate,name="reject_candidate"),
    path('Logout',Logout,name="Logout"),
    path('forgot_password_candidate', forgot_password_candidate, name='forgot_password_candidate'),
    path('forgot_password_recruiter', forgot_password_recruiter, name='forgot_password_recruiter'),
    # url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
 
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
