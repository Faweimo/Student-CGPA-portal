from django.contrib import admin
from .models import  *

# Course Admin display /
class CourseAdmin(admin.ModelAdmin):
    list_display = ('profile','course_name','course_code','credit_unit')
    # def save_model(self, request, obj, form, change):
    #     obj.added_by = request.user
    #     super().save_model(request, obj, form, change)

admin.site.register(Course,CourseAdmin)

# Result Admin display 
class ResultAdmin(admin.ModelAdmin):
    list_display = ('course','score','grade','points','unit_points', )

admin.site.register(Result,ResultAdmin)

admin.site.register(CGPA)
admin.site.register(StudentCourse)
admin.site.register(LevelAndSemester)