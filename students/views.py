from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Student, Achievement
from .forms import StudentForm, AchievementForm

class DashboardView(TemplateView):
    template_name = 'students/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_students'] = Student.objects.count()
        context['active_students'] = Student.objects.filter(status='Active').count()
        context['total_achievements'] = Achievement.objects.count()
        return context

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(register_number__icontains=query) |
                Q(department__icontains=query)
            )
        return queryset

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

class AchievementCreateView(LoginRequiredMixin, CreateView):
    model = Achievement
    form_class = AchievementForm
    template_name = 'students/achievement_form.html'

    def get_initial(self):
        initial = super().get_initial()
        student_id = self.request.GET.get('student')
        if student_id:
            initial['student'] = get_object_or_404(Student, pk=student_id)
        return initial

    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.object.student.pk})

class AchievementUpdateView(LoginRequiredMixin, UpdateView):
    model = Achievement
    form_class = AchievementForm
    template_name = 'students/achievement_form.html'
    
    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.object.student.pk})

from django.contrib.auth.decorators import login_required

@login_required
def approve_achievement(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    achievement.status = 'Approved'
    achievement.save()
    return redirect('student_detail', pk=achievement.student.pk)

@login_required
def reject_achievement(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    achievement.status = 'Rejected'
    achievement.save()
    return redirect('student_detail', pk=achievement.student.pk)

class AchievementDeleteView(LoginRequiredMixin, DeleteView):
    model = Achievement
    template_name = 'students/achievement_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.object.student.pk})
