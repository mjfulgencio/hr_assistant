from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('', views.landing_page, name='landing_page'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('employee_form', views.employee_form, name='employee_form'),
    path('employee_list', views.employee_list, name='employee_list'),
    path('training', views.training, name='training'),
    path('demographics', views.demographics, name='demographics'),
    path('calendar', views.calendar, name='calendar'),
    path('kanban', views.kanban, name='kanban'),
    path('account', views.account, name='account')
]