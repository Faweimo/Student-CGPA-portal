from unittest import result
from django.db.models.signals import post_save, pre_delete,pre_save
from django.dispatch import receiver

from accounts.models import Profile, User
from .models import CGPA, Course, Result, StudentCourse


# when course is created also create result /
@receiver(post_save, sender=Course) 
def create_result(sender, instance, created,*args, **kwargs):
    if created:        
        Result.objects.create(course=instance)
        instance.save()
     

# when student course is created, also create the instance of the cgpa
@receiver(post_save,sender=StudentCourse)
def create_cgpa(sender, instance,created,*args,**kwargs):
    if created:
        CGPA.objects.create(student_course=instance)
        instance.save()


# if profile is created, create an instance of studentcourse
@receiver(post_save, sender=Profile)
def create_cgpa(sender, instance,created,*args,**kwargs):
    if created:
        studentcourse = StudentCourse.objects.create(profile=instance)
        CGPA(profile=instance,student_course=studentcourse)
        instance.save()