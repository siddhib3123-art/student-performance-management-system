from django.urls import path
from .import views
urlpatterns =[
    path('',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('students/',views.show_students,name='show_students'),
    path('add/',views.add_student,name='add_student'),
    path('update/<str:roll>/',views.update_student,name='update_student'),
    path('delete/<str:roll>/',views.delete_student,name='delete_student'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),

]