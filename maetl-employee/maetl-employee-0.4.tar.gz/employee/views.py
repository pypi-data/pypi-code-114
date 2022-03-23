import datetime
from django.shortcuts import render, redirect, get_object_or_404

import employee
from .models import *
from .forms import EmployeeForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from .utils import *
from itertools import chain
from django.urls import reverse_lazy
from .forms import *
from custom.utils import *
from django.http import JsonResponse
from django.utils import timezone
import datetime
from population.utils import getlastid_kinos, getlastid_kinosuser
from development.models import *


def AdminEmployeeDashboard(request):
    group = request.user.groups.all()[0].name
    context = {
        'group': group,
        'title': 'Lista Empregu'
    }
    return render(request, 'employee/dashboard.html', context)


@login_required
def xefe_charts(request):
    # currentYear = date.today().year
    try:
        empuser = EmployeeUser.objects.get(user=request.user)
        employee = Employee.objects.get(employeeuser=empuser)
    except:
        print('You are admin')
    querysets = None
    labels = []
    data = []
    employee = Employee.objects.all()
    empuser = EmployeeUser.objects.filter(
        employee__in=employee, user__groups__name='xefe')
    municipality = Municipality.objects.all()
    for m in municipality:
        querysets = Employee.objects.filter(
            id__in=empuser, municipality=m, is_active=True).all().count()
        labels.append(m.name)
        data.append(querysets)
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


@login_required
def sec_charts(request):
    # currentYear = date.today().year
    try:
        empuser = EmployeeUser.objects.get(user=request.user)
        employee = Employee.objects.get(employeeuser=empuser)
    except:
        print('You are admin')
    querysets = None
    labels = []
    data = []
    employee = Employee.objects.all()
    empuser = EmployeeUser.objects.filter(
        employee__in=employee, user__groups__name='sec')
    municipality = Municipality.objects.all()
    for m in municipality:
        querysets = Employee.objects.filter(
            id__in=empuser, municipality=m, is_active=True).all().count()
        labels.append(m.name)
        data.append(querysets)
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


@login_required
def AdminEmployeeAdd(request):
    group_user = Group.objects.all()
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        id_suku = request.POST.get('village')

        newid = getlastid_kinos(Employee,id_suku)
        # newid2 = getjustnewid(User)
        newid3 = getlastid_kinosuser(EmployeeUser,id_suku)


        print(request.POST.get('village'))
        form = EmployeeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid  # 4
            instance.datetime = datetime.datetime.now()
            # instance.hashed = new_hashid
            instance.user = request.user
            instance.save()
            username = split_string(form.cleaned_data.get(
                'first_name'))+str(newid)  # maria4
            password = make_password('Mae@2021')
            print(instance.village.id)
            obj2 = User(id=newid, username=username, password=password)  # 7
            obj2.save()
            obj3 = EmployeeUser(id=newid3, user_id=newid, employee_id=newid)
            obj3.save()
            group_user = Group.objects.get(name=request.POST.get('group_name'))
            user = User.objects.get(pk=newid)
            user.groups.add(group_user)
            # messages.success(request, f'New employee has been added.')
            return redirect('employee:admin-employee-dashboard')
    else:
        form = EmployeeForm()
    context = {
        'form': form, 'group': group,
        'title': 'Aumenta Empregu', 'legend': 'Aumenta Empregu'
    }
    return render(request, 'employee/add.html', context)


@login_required
def AdminListXefe(request):
    group = request.user.groups.all()[0].name
    employee = []
    emp = Employee.objects.filter(
        employeeuser__user__groups__name='xefe', is_active=True).order_by('municipality__name')
    for i in emp:
        e2 = EmployeeUser.objects.filter(employee__id=i.id)
        for e in e2:
            employee.append([e.user, i])
    context = {
        'title': 'Lista Xefe Suku', 'legend': 'Lista Xefe Suku', 'group': group,
        'employee': employee
    }
    return render(request, 'employee/list_xefe.html', context)


@login_required
def AdminListSec(request):
    group = request.user.groups.all()[0].name
    employee = []
    emp = Employee.objects.filter(
        employeeuser__user__groups__name='sec', is_active=True).order_by('municipality__name')
    for i in emp:
        e2 = EmployeeUser.objects.filter(employee__id=i.id)
        for e in e2:
            employee.append([e.user, i])
    context = {
        'title': 'Lista PAAS', 'legend': 'Lista PAAS', 'group': group,
        'employee': employee
    }
    return render(request, 'employee/list_sec.html', context)

# EMPLOYEE


@login_required
def EmployeeDetail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Employee, hashed=hashid)

    context = {
        'hashid': hashid, 'objects': objects,
        'group': group,
        'title': 'Detalha Empregu', 'legend': 'Detalha Empregu'
    }
    return render(request, 'employee/detail.html', context)


@login_required
def EmployeeUpdate(request, hashid):
    objects = get_object_or_404(Employee, hashed=hashid)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=objects)
        if form.is_valid():
            form.save()
            # messages.success(request, f'Employee information has been updated.')
            return redirect('employee:employee-detail', hashid=hashid)
    else:
        form = EmployeeForm(instance=objects)
    context = {
        'form': form,
        'title': 'Altera Informasaun Empregu', 'legend': 'Altera Informasaun Empregu'
    }
    return render(request, 'employee/add.html', context)


@login_required
def EmployeeTerminate(request, hashid):
    objects = get_object_or_404(Employee, hashed=hashid)
    empuser = get_object_or_404(EmployeeUser, employee=objects)
    user = User.objects.get(username=empuser.user.username)
    user.is_active = False
    user.save()
    objects.is_end = True
    objects.is_active = False
    objects.end_period = datetime.datetime.now()
    objects.save()
    return redirect('employee:admin-employee-dashboard')


# USER MANAGEMENT
@login_required
def AccountUpdate(request):
    # objects = EmployeeUser.objects.get(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            # messages.success(request, f'Your account has been updated!')
            return redirect('employee:user-account')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
        'title': 'ACCOUNT INFO',
        'legend': 'ACCOUNT INFO',
    }
    return render(request, 'user/account.html', context)


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'user/change_password.html'
    success_url = reverse_lazy('employee:user-change-password-done')


class UserPasswordChangeDoneView(PasswordResetDoneView):
    template_name = 'user/change_password_done.html'
