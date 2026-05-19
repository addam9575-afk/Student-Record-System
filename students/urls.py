from django.urls import path
from . import views
from .dashboard_views import dashboard
from .auth_views import signup_view, login_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('', views.StudentListView.as_view(), name='student_list'),
    path('add/', views.StudentCreateView.as_view(), name='student_add'),
    path('edit/<int:pk>/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('dashboard/', dashboard, name='dashboard'),
]
