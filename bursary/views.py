from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group



# Create your views here.

from .models import *
from .forms import ApplicationForm, CreateUserForm, StudentForm
from .filters import ApplicationFilter
from .decorators import unauthenticated_user,allowed_users,admin_only

@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
               user = form.save()
               username = form.cleaned_data.get('username')
               messages.success(request, 'Account Created For' + username)

               return redirect('login')

    context = {'form':form}
    return render(request,'bursary/register.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,'Username OR Password is Incorrect')

    context = {}
    return render(request, 'bursary/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def dashboard(request):
    applications = Applications.objects.all()
    students = Student.objects.all()

    total_applications = applications.count()
    disbursed_bursaries = applications.filter(status='Fully Disbursed').count()
    pending_bursaries = applications.filter(status='Pending').count()
    in_progress = applications.filter(status='Disbursement in Progress').count()

    myFilter = ApplicationFilter(request.GET, queryset=applications)
    applications = myFilter.qs

    context = {'applications': applications, 'students': students, 'total_applications': total_applications,
               'disbursed_bursaries': disbursed_bursaries, 'pending_bursaries': pending_bursaries,
               'in_progress':in_progress, 'myFilter':myFilter}

    return render(request, 'bursary/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def userPage(request):
    applications = request.user.student.applications.all()
    print('APPLICATIONS:',applications)

    total_applications = applications.count()
    disbursed_bursaries = applications.filter(status='Fully Disbursed').count()
    pending_bursaries = applications.filter(status='Pending').count()
    in_progress = applications.filter(status='Disbursement in Progress').count()

    context = {'applications':applications, 'total_applications': total_applications,
               'disbursed_bursaries': disbursed_bursaries, 'pending_bursaries': pending_bursaries,'in_progress':in_progress}
    return render(request,'bursary/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def accountApplyBursary(request):
    student = request.user.student
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'bursary/apply_bursary.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def bursaries(request,):
    bursaries = Bursary.objects.all()
    return render(request, 'bursary/bursaries.html', {'bursaries': bursaries})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def student(request, pk_test):
    student = Student.objects.get(id=pk_test)
    applications = student.applications.all()
    application_count = applications.count()

    myFilter = ApplicationFilter(request.GET, queryset=applications)
    applications = myFilter.qs

    context = {'student': student, 'applications': applications, 'application_count': application_count,'myFilter':myFilter}
    return render(request, 'bursary/student.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createApplication(request,pk):
    ApplicationFormSet = inlineformset_factory(Student,Applications, fields=('bursary','status','applyAmount'), extra=6)
    student = Student.objects.get(id=pk)
    formset = ApplicationFormSet(queryset=Applications.objects.none(),instance=student)
    #form = ApplicationForm(initial={'student':student})
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        #form = ApplicationForm(request.POST)
        formset = ApplicationFormSet(request.POST, instance=student)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    return render(request, 'bursary/apply_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateApplication(request,pk):
    application = Applications.objects.get(id=pk)
    form = ApplicationForm(instance=application)
    if request.method == "POST":
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'bursary/update_bursary.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteApplication(request,pk):
    application = Applications.objects.get(id=pk)
    if request.method == "POST":
        application.delete()
        return redirect('/')

    context = {'item':application}
    return render(request, 'bursary/delete.html', context)
