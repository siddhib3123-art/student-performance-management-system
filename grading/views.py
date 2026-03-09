from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student
from django.contrib import messages
from django.db.models import Q, Avg
def login_view(request):
     if request.method == "POST":
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(request, username=username, password=password)
         if user is not None:
             login(request, user)
             return redirect('home')
         else:
             messages.error(request,'Invalid username or passwoed')
     return render(request,'login.html')
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
#  HOME
@login_required
def home(request):
    students = Student.objects.all()
    total_students = students.count()
    pass_count = students.filter(percentage__gte=50).count()
    fail_count = students.filter(percentage__lt=50).count()
    avg_percentage = 0
    if total_students > 0:
        avg_percentage = sum([s.percentage for s in students]) / total_students
    context = {
        'total_students': total_students,
        'pass_count': pass_count,
        'fail_count': fail_count,
        'avg_percentage': avg_percentage
    }
    return render(request, 'home.html', context)
#DASHBOARD
@login_required
def dashboard(request):
    students = Student.objects.all()
    total_students = students.count()
    pass_count  = students.filter(percentage__gte=50).count()
    fail_count = students.filter(percentage__lt=50).count()
    topper = students.order_by('-percentage').first()
    avg_percentage = 0
    if total_students > 0:
        avg_percentage = sum([s.percentage for s in students]) / total_students
    context = {
        'total_students' : total_students,
        'pass_count' : pass_count,
        'fail_count' : fail_count,
        'topper' : topper,
        'avg_percentage' : avg_percentage
    }
    return  render(request,'dashboard.html',context)


#SHOW STUDENTS
@login_required()
def show_students(request):
    query = request.GET.get('q', '')
    if query:
        students = Student.objects.filter(roll__icontains=query) | Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()
    return render(request,'show_students.html',{'students':students})
#ADD STUDENT
@login_required
def add_student(request):
    if request.method == "POST":
            roll = request.POST.get('roll')
            name = request.POST.get('name')
            english=int(request.POST.get('english'))
            maths = int(request.POST.get('maths'))
            science = int(request.POST.get('science'))
            socialscience = int(request.POST.get('socialscience'))
            marathi = int(request.POST.get('marathi'))
            Student.objects.create(
                name=name,
                roll=roll,
                english=english,
                maths=maths,
                science=science,
                socialscience=socialscience,
                marathi=marathi
            )
            return redirect('show_students')
    return render(request,'add_student.html')

#UPDATE STUDENT
@login_required
def update_student(request,roll):
    #Get student by roll number
    student = get_object_or_404(Student, roll=roll)
    if request.method == "POST":
        student.name = request.POST.get('name')
        student.english =int(request.POST.get('english'))
        student.maths = int(request.POST.get('maths'))
        student.science = int(request.POST.get('science'))
        student.socialscience = int(request.POST.get('socialscience'))
        student.marathi = int(request.POST.get('marathi'))
        student.save()  #model auto calculates or recalculates total , percentage , grade
        return redirect('show_students')
    return render(request,'update_student.html',{'student':student})
# #DELETE STUDENT
@login_required
def delete_student(request,roll):
    student = get_object_or_404(Student,roll=roll)
    if request.method == "POST":
        student.delete()
        return redirect('show_students')
    return render(request,'delete_student.html',{'student':student})


