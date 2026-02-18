from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/add/', views.StudentCreateView.as_view(), name='student_add'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    
    path('achievements/add/', views.AchievementCreateView.as_view(), name='achievement_add'),
    path('achievements/<int:pk>/edit/', views.AchievementUpdateView.as_view(), name='achievement_edit'),
    path('achievements/<int:pk>/delete/', views.AchievementDeleteView.as_view(), name='achievement_delete'),
    path('achievements/<int:pk>/approve/', views.approve_achievement, name='approve_achievement'),
    path('achievements/<int:pk>/reject/', views.reject_achievement, name='reject_achievement'),

    path('login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
