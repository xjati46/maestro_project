from django.contrib import admin
from student_app.models import Student, Rapor
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'id', 'nama_lengkap')


@admin.register(Rapor)
class RaporAdmin(admin.ModelAdmin):
    pass
