from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('courses/', views.courses, name='courses'),
   path('courseDetail/<int:id>', views.courseDetail, name='detail'),
   path('assignments/', views.assignments, name='assignments'),
   path('assignmentDetail/<int:id>', views.assignmentDetail, name='detail'),
   path('newcourse/', views.newCourse, name='newcourse'),
   path('newassignment/', views.newAssignment, name='newassignment'),
   path('loginmessage/', views.loginmessage, name='loginmessage'),
   path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]