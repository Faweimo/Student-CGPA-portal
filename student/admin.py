from django.contrib import admin
from .models import  *

# Course Admin display /
class CourseAdmin(admin.ModelAdmin):
    list_display = ('profile','course_name','course_code','credit_unit')

admin.site.register(Course,CourseAdmin)

# Result Admin display 
class ResultAdmin(admin.ModelAdmin):
    list_display = ('course','score','grade','points','unit_points', )

admin.site.register(Result,ResultAdmin)

admin.site.register(CGPA)
admin.site.register(StudentCourse)
admin.site.register(LevelAndSemester)