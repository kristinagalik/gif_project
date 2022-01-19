from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from databank_system.models import NewBilling, NewRecord, UserInfo
from databank_system.forms import UserForm, NewBillingForm, NewRecordForm
from django.urls import reverse
from django.contrib.auth.models import User


def home_page(request):
    if request.user.is_authenticated:
        return render(request, 'databank_system/home_page.html', )
    else:
        return redirect(reverse('databank_system:user_login'))


def all_records(request):
    context_dic = {}

    records = NewRecord.objects.all()
    context_dic["records"] = records

    print(context_dic)
    return render(request, 'databank_system/all_records.html', context_dic)


@login_required
def new_record(request):
    if request.method == 'POST':
        form = NewRecordForm(request.POST)

        if form.is_valid():
            record_object = form.save(commit=False)
            record_object.save()
            return redirect('databank_system:all_records')

        else:
            print(form.errors)

    return render(request, 'databank_system/new_record.html', )


def record(request):
    return render(request, 'databank_system/record.html', )


def all_billings(request):
    context_dic = {}

    billings = NewBilling.objects.all()
    context_dic["billings"] = billings

    print(context_dic)

    return render(request, 'databank_system/all_billings.html', context_dic)


@login_required
def new_billing(request):
    if request.method == 'POST':
        form = NewBillingForm(request.POST)

        if form.is_valid():
            billing_object = form.save(commit=False)
            billing_object.save()

            return redirect('databank_system:all_billings')

        else:
            print(form.errors)

    return render(request, 'databank_system/new_billing.html', )


def billing(request):
    return render(request, 'databank_system/billing.html', )


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                # Will login the user and return them to the login page.
                login(request, user)
                return redirect(reverse('databank_system:home_page'))
            else:
                # If an inactive account was used then it prevents login.
                return HttpResponse("Account is disabled")

        else:
            # If the login details were incorrect then it doesn't log the user in.
            print("Invalid username or password.")
            return HttpResponse("Account details incorrect.")

    else:
        # If request was not HTTP POST, will just return user to login page.
        return render(request, 'databank_system/login.html', )


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('databank_system:user_login'))
