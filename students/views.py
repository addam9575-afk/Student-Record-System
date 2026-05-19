from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from .models import Student
from .forms import StudentForm


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_queryset(self):
        queryset = Student.objects.all()
        search_query = self.request.GET.get('search', '')
        course_filter = self.request.GET.get('course', '')
        marks_filter = self.request.GET.get('marks', '')

        if search_query:
            queryset = queryset.filter(
                name__icontains=search_query
            ) | queryset.filter(
                roll_number__icontains=search_query
            )

        if course_filter:
            queryset = queryset.filter(course__icontains=course_filter)

        if marks_filter:
            try:
                min_marks = float(marks_filter)
                queryset = queryset.filter(marks__gte=min_marks)
            except ValueError:
                pass

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['course_filter'] = self.request.GET.get('course', '')
        context['marks_filter'] = self.request.GET.get('marks', '')
        context['total_students'] = Student.objects.count()
        context['average_marks'] = round(
            Student.objects.aggregate(avg=Avg('marks'))['avg'] or 0, 2
        )
        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        messages.success(self.request, 'Student added successfully!')
        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        messages.success(self.request, 'Student updated successfully!')
        return super().form_valid(form)


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        messages.success(self.request, 'Student deleted successfully!')
        return super().form_valid(form)
