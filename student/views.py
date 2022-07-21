from calendar import c
from django.shortcuts import render

from accounts.models import Profile, User
from student.models import CGPA, Course, LevelAndSemester, Result,StudentCourse
from django.db.models import Sum,Max

def index(request):
    user = StudentCourse.objects.all()
    # cgpa = CGPA.objects.all().aggregate(Max('cgpa'))['cgpa__max']
    cgpa = CGPA.objects.all().order_by('-cgpa')
    print(cgpa)
    high_cgpa = None
    for x in cgpa:
        if high_cgpa and high_cgpa != x.cgpa:
            break
        high_cgpa = x.cgpa 
        print(high_cgpa)
    context ={
        'cgpa':cgpa
    }
    return render(request, 'student/overall_best.html',context)