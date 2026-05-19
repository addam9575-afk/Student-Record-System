from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from .models import Student


@login_required
def dashboard(request):
    total_students = Student.objects.count()
    average_marks = Student.objects.aggregate(avg_marks=Avg('marks'))['avg_marks'] or 0
    top_students = Student.objects.order_by('-marks')[:5]

    context = {
        'total_students': total_students,
        'average_marks': round(average_marks, 2),
        'top_students': top_students,
    }
    return render(request, 'students/dashboard.html', context)
