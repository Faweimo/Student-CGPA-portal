from unittest import result
from django.db import models
from accounts.models import Department, User,Profile

from django.db.models import Sum

# ItemPrice.objects.aggregate(Sum('price'))
#  def total_score(self):
#        return self.climbs_completed.aggregate(total_score=Sum('points'))['total_score']

class LevelAndSemester(models.Model):
    level_choices = (
        (100, '100level'),
        (200,'200level'),
        (300, '300level'),
        (400, '400level'),
        (500, '500level')
    )
    level = models.PositiveSmallIntegerField(
        
        choices=level_choices
    )

    semester_choices = (
        (1, 'first semester'),
        (2, 'second semester')
    )

    semester = models.PositiveSmallIntegerField(
        
        choices=semester_choices
        )


    def __str__(self):
        return f'{self.level} - {self.semester}'

    class Meta:
        
        verbose_name = 'Level And Semester'
        verbose_name_plural = 'Level And Semesters'

'''
Courses of the students
'''        
class Course(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
        )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    leave_and_semester = models.ForeignKey(
        LevelAndSemester,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    course_name = models.CharField(
        max_length=250
    )
    course_code = models.CharField(
        max_length=250,
        blank=True,
        null=True
    )
    credit_unit = models.PositiveIntegerField(
        blank=True,
        null=True
    )
 
    def __str__(self):
        return f'{self.profile} || {self.course_name} - {self.course_code}'

    class Meta:
        
        verbose_name = 'course'
        verbose_name_plural = 'courses'



# Result model
class Result(models.Model):

    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    grade = models.CharField(max_length=50, blank=True,null=True,editable=False)
    points = models.PositiveIntegerField(default=0,editable=False)
    unit_points = models.PositiveIntegerField( blank=True,null=True,editable=False)
    
    def __str__(self):
        return f'{self.course}'

    class Meta:
        
        verbose_name = 'result'
        verbose_name_plural = 'results'

    # override the save method and automate the fields
    def save(self, *args,**kwargs):
        '''
        get the score value and grade it equivalent to their points 
        Note that : A = 5 POINTS, B=4 POINTS, C=3POINTS ,D=2POINTS, E=1POINT,F=0POINT
        '''
        
        if self.score >= 0 and self.score <=39:
            self.grade = 'F'
            self.points = 0
            self.unit_points = self.points * self.course.credit_unit
        elif self.score >=40 and self.score <= 44 :
            self.grade = 'E'
            self.points = 1 
            self.unit_points = self.points * self.course.credit_unit
        elif self.score >= 45 and self.score <= 49:
            self.grade = 'D'
            self.points = 2
            self.unit_points = self.points * self.course.credit_unit 
        elif self.score >= 50 and self.score <= 59:
            self.grade = 'C'
            self.points = 3   
            self.unit_points = self.points * self.course.credit_unit  
        elif self.score >= 60 and self.score <= 69:
            self.grade = 'B'
            self.points = 4          
            self.unit_points = self.points * self.course.credit_unit
        elif self.score >= 70 and self.score <= 100:
            self.grade = 'A'
            self.points = 5 
            self.unit_points = self.points * self.course.credit_unit  
        else:
            self.grade = 'score are rated over 100'
            self.points = 0        
            self.unit_points = 0
        super(Result,self).save(*args,**kwargs)


# Student total course     
class StudentCourse(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
        )
    result = models.ManyToManyField(
        Result
        
    )
    created_at=models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return f'{self.profile}'

    class Meta:
        verbose_name = 'Student Course'
        verbose_name_plural = 'Student Courses'
            

# CGPA model 
class CGPA(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    student_course = models.OneToOneField(
        StudentCourse,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    ) 
    total_credit_units = models.IntegerField(default=0,blank=True,null=True)
        
    total_unit_points = models.IntegerField(default=0,blank=True,null=True)
        
    cgpa = models.DecimalField(
        decimal_places=2,
        max_digits=3,
        default=0
    )

    def __str__(self):
        return f'{self.student_course}'

    def save(self,*args,**kwargs):

        # get the overall unit point of each student relating to their department and courses taken /
        profile = Profile.objects.get(user=self.student_course.profile.user)
        course = Course.objects.filter(profile=profile)
        r = Result.objects.filter(course__id__in=course).aggregate(Sum('unit_points'))['unit_points__sum']
        
        # get the total unit points field and save the sum of unit * points of the result
        self.total_unit_points=r

        # get the overall credit unit of each student relating to their department and courses taken /
        c = Course.objects.filter(profile=profile).aggregate(Sum('credit_unit'))['credit_unit__sum']

        # get the total credit units field and save the sum of the credit unit of the course
        self.total_credit_units=c

        if self.total_credit_units and self.total_unit_points:

            self.cgpa=self.total_unit_points/self.total_credit_units
            
            d = round(float(self.cgpa),2)
        
        super(CGPA,self).save(*args,**kwargs)
        
   
    class Meta:
        
        verbose_name = 'CGPA'
        verbose_name_plural = 'CGPAs'