from django.contrib import admin
from student_app.models import Student, Rapor

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Rapor)
class RaporAdmin(admin.ModelAdmin):
    pass
