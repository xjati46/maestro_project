from django.contrib import admin
from coach_app.models import *

# Register your models here.


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('nama_panggilan', 'alamat_kotakab', 'nomor_ponsel')
