from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth import authenticate,login

from accounts.utils import matric_no
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from student.models import *
from itertools import chain


# Get the total unit points

def get_total_unit_points(self):
    user = User.objects.get(id=self.user.id)
    profile = Profile.objects.get(user=user)
    level = LevelAndSemester.objects.all()
    course = Course.objects.filter(profile=profile).filter(leave_and_semester__id__in=level)
    r = Result.objects.filter(course__id__in=course).aggregate(Sum('unit_points'))['unit_points__sum']
    return r

#user dashboard 
@login_required(login_url='login')
def dashboard(request):
    user = User.objects.get(id=request.user.id)
    if not user:
        return HttpResponse('Log in to your dashboard')
    else:    
        profile = Profile.objects.get(user=request.user)
        level = LevelAndSemester.objects.all()
        course = Course.objects.filter(profile=profile).filter(leave_and_semester__id__in=level).order_by('-leave_and_semester')
        result = Result.objects.filter(course__id__in=course).order_by('-course')
        studentcourse = StudentCourse.objects.filter(result__id__in=result).all().distinct()
        cgpa = CGPA.objects.get(student_course__in=studentcourse)
        if not cgpa:
            return HttpResponse('User has no CGPA')
        context = {
            'result':result,
            'course':course,
            'profile':profile,
            'studentcourse':studentcourse,
            'cgpa':cgpa
        }  
    return render(request,'accounts/user/dashboard.html',context)


# Log out view
@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out.')
    return redirect('login')