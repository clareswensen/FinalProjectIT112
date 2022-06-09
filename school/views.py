from django.shortcuts import render
from .models import Course, Assignment
from django.shortcuts import render, get_object_or_404
from .forms import CourseForm, AssignmentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'school/index.html')

def courses(request):
    course_list=Course.objects.all()
    return render(request, 'school/courses.html', {'course_list': course_list})

def assignments(request):
    assignment_list=Assignment.objects.all()
    return render(request, 'school/assignments.html', {'assignment_list': assignment_list})

def courseDetail(request, id):
    course=get_object_or_404(Course, pk=id)
    return render(request, 'school/coursedetail.html', {'course': course})

def assignmentDetail(request, id):
    assignment=get_object_or_404(Assignment, pk=id)
    return render(request, 'school/assignmentdetail.html', {'assignment': assignment})

@login_required
def newCourse(request):
    form=CourseForm

    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
                post=form.save(commit=True)
                post.save()
                form=CourseForm()
    else:
        form=CourseForm()
    return render(request, 'school/newcourse.html', {'form': form})

@login_required
def newAssignment(request):
    form=AssignmentForm

    if request.method=='POST':
        form=AssignmentForm(request.POST)
        if form.is_valid():
                post=form.save(commit=True)
                post.save()
                form=AssignmentForm()
    else:
        form=AssignmentForm()
    return render(request, 'school/newassignment.html', {'form': form})

def loginmessage(request):
    return render(request, 'school/loginmessage.html')

def logoutmessage(request):
    return render(request, 'school/logoutmessage.html')
