from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from databank_system.models import Billing, Record, UserInfo
from databank_system.forms import UserForm, BillingForm, RecordForm
from django.urls import reverse
from django.contrib.auth.models import User
from databank_system.forms import BillingUpdateForm, RecordUpdateForm


def home_page(request):
    if request.user.is_authenticated:
        context_dic = {}
        records = list(Record.objects.all())
        billings = list(Billing.objects.all())
        context_dic["objects"] = records + billings
        context_dic["objects"] = sorted(context_dic["objects"], key=lambda d: d.date, reverse=True)
        return render(request, 'databank_system/home_page.html', context_dic)
    else:
        return redirect(reverse('databank_system:user_login'))


def all_records_default(request):
    return redirect('databank_system:all_records', 'date')


def all_records(request, order_by="date"):
    if request.user.is_authenticated:
        context_dic = {}
        records = Record.objects.all()

        if order_by == "date":
            context_dic["records"] = records.order_by('-date')
        if order_by == "project":
            context_dic["records"] = records.order_by('project')
        if order_by == "worker":
            context_dic["records"] = records.order_by('worker')

        return render(request, 'databank_system/all_records.html', context_dic)
    else:
        return redirect(reverse('databank_system:user_login'))


def new_record(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = RecordForm(request.POST)

            if form.is_valid():
                record_object = form.save(commit=False)
                record_object.save()
                return redirect('databank_system:all_records', 'date')

            else:
                print(form.errors)

        return render(request, 'databank_system/new_record.html')

    else:
        return redirect(reverse('databank_system:user_login'))


def single_record(request, id):
    if request.user.is_authenticated:
        context_dict = {}
        try:
            context_dict['record'] = Record.objects.get(id=id)

        except Record.DoesNotExist:
            context_dict['record'] = None
        return render(request, 'databank_system/single_record.html', context_dict)
    else:
        return redirect(reverse('databank_system:user_login'))


def delete_record(request, id):
    Record.objects.filter(id=id).delete()
    return redirect('databank_system:all_records', 'date')


def all_billings_default(request):
    return redirect('databank_system:all_billings', 'date')


def all_billings(request, order_by="date"):
    if request.user.is_authenticated:
        context_dic = {}
        billings = Billing.objects.all()

        if order_by == "date":
            context_dic["billings"] = billings.order_by('-date')
        if order_by == "budget_code":
            context_dic["billings"] = billings.order_by('budget_code')
        if order_by == "worker":
            context_dic["billings"] = billings.order_by('worker')

        return render(request, 'databank_system/all_billings.html', context_dic)
    else:
        return redirect(reverse('databank_system:user_login'))


def new_billing(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BillingForm(request.POST)

            if form.is_valid():
                billing_object = form.save(commit=False)
                billing_object.save()

                return redirect('databank_system:all_billings', 'date')

            else:
                print(form.errors)

        return render(request, 'databank_system/new_billing.html', )
    else:
        return redirect(reverse('databank_system:user_login'))


def single_billing(request, id):
    if request.user.is_authenticated:
        context_dict = {}
        try:
            context_dict['billing'] = Billing.objects.get(id=id)

        except Billing.DoesNotExist:
            context_dict['billing'] = None
        return render(request, 'databank_system/single_billing.html', context_dict)
    else:
        return redirect(reverse('databank_system:user_login'))


def delete_billing(request, id):
    Billing.objects.filter(id=id).delete()
    return redirect('databank_system:all_billings', 'date')


def single_billing_edit(request, id):
    if request.user.is_authenticated:
        context_dic = {}
        current_billing = Billing.objects.get(id=id)
        context_dic["billing"] = current_billing
        if request.method == 'POST':
            billing_form = BillingUpdateForm(request.POST)
            if billing_form.is_valid():
                current_billing.date = request.POST.get('date', "")
                current_billing.worker = request.POST.get('worker', "")
                current_billing.budget_code = request.POST.get('budget_code', "")
                current_billing.project = request.POST.get('project', "")
                current_billing.unit = request.POST.get('unit', "")
                current_billing.cost = request.POST.get('cost', "")

                current_billing.save()
                return redirect('/')

        return render(request, 'databank_system/single_billing_edit.html', context_dic)
    else:
        return redirect(reverse('databank_system:user_login'))


def single_record_edit(request, id):
    if request.user.is_authenticated:
        context_dic = {}
        current_record = Record.objects.get(id=id)
        context_dic["record"] = current_record
        if request.method == 'POST':
            record_form = RecordUpdateForm(request.POST)
            if record_form.is_valid():
                current_record.date = request.POST["date"]
                current_record.worker = request.POST["worker"]
                current_record.project = request.POST["project"]
                current_record.budget_code = request.POST["budget_code"]
                current_record.email = request.POST["email"]
                current_record.contact_tel_no = request.POST["contact_tel_no"]
                current_record.procedure = request.POST["procedure"]
                current_record.chemical_fixation = request.POST["chemical_fixation"]
                current_record.negstaining = request.POST["negstaining"]
                current_record.cryofixation = request.POST["cryofixation"]
                current_record.tem_embedding_schedule = request.POST["tem_embedding_schedule"]
                current_record.sem = request.POST["sem"]
                current_record.dehydration = request.POST["dehydration"]
                current_record.sem_mount = request.POST["sem_mount"]
                current_record.fd = request.POST["fd"]
                current_record.cpd = request.POST["cpd"]
                current_record.resin = request.POST["resin"]
                current_record.sem_cost = request.POST["sem_cost"]
                current_record.temp_time = request.POST["temp_time"]
                current_record.immunolabeling = request.POST["immunolabeling"]
                current_record.ab_dilution_time = request.POST["ab_dilution_time"]
                current_record.ab_gold_dilution_time = request.POST["ab_gold_dilution_time"]
                current_record.contrast_staining = request.POST["contrast_staining"]
                current_record.comment = request.POST["comment"]

                current_record.save()
                return redirect('/')

        return render(request, 'databank_system/single_record_edit.html', context_dic)
    else:
        return redirect(reverse('databank_system:user_login'))


def user_login(request, user_details_incorrect=False):
    if not request.user.is_authenticated:
        context_dic = {}
        context_dic['user_details_incorrect'] = user_details_incorrect
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
                    return HttpResponse("Account is disabled.")

            else:
                # If the login details were incorrect then it doesn't log the user in.
                context_dic['user_details_incorrect'] = True
                return render(request, 'databank_system/login.html', context_dic)

        else:
            # If request was not HTTP POST, will just return user to login page.
            return render(request, 'databank_system/login.html', context_dic)
    else:
        return redirect(reverse('databank_system:home_page'))


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('databank_system:user_login'))
