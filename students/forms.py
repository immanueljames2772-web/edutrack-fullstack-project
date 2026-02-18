from django import forms
from .models import Student, Achievement

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['student', 'title', 'description', 'proof', 'category', 'date', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
