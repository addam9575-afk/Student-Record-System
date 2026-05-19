from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll_number', 'email', 'course', 'marks', 'created_at']
    list_filter = ['course', 'marks']
    search_fields = ['name', 'roll_number']
    ordering = ['-marks']
    date_hierarchy = 'created_at'
