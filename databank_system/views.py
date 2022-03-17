from databank_system.forms import BillingUpdateForm, RecordUpdateForm
from databank_system.forms import UserForm, BillingForm, RecordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from databank_system.models import Billing, Record
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse
import csv


"""
    Homepage view displays all the billings and records sorted by date at the home page.
"""


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


"""
    All records default view displays list of records by date, if it isn't specified, by what to sort the records.
"""


def all_records_default(request):
    if request.user.is_authenticated:
        return redirect('databank_system:all_records', 'date')
    else:
        return redirect(reverse('databank_system:user_login'))

"""
    Mobile menu is a view for page that appears on mobile devices, that supplements navigation bar.
"""


def mobile_menu(request):
    if request.user.is_authenticated:
        return render(request, 'databank_system/mobile_menu.html')
    else:
        return redirect(reverse('databank_system:user_login'))


"""
    All records view displays records after it has been chosen, by what to sort them.
"""


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


"""
    New record view displays page with form that allows users to create new instances of record model.
"""


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


"""
    Single record view displays page with chosen record and all its details, additionally with 'edit' and 'delete' buttons.
"""


def single_record(request, id):
    if request.user.is_authenticated:
        context_dic = {}
        try:
            context_dic['record'] = Record.objects.get(id=id)

        except Record.DoesNotExist:
            context_dic['record'] = None
        return render(request, 'databank_system/single_record.html', context_dic)
    else:
        return redirect(reverse('databank_system:user_login'))


"""
    Delete record view deletes a chosen instance of record model.
"""


def delete_record(request, id):
    if request.user.is_authenticated:
        Record.objects.filter(id=id).delete()
        return redirect('databank_system:all_records', 'date')
    else:
        return redirect(reverse('databank_system:user_login'))

"""
    All billings default view displays list of billings by date, if it isn't specified, by what to sort the billings.
"""


def all_billings_default(request):
    if request.user.is_authenticated:
        return redirect('databank_system:all_billings', 'date')
    else:
        return redirect(reverse('databank_system:user_login'))

"""
    All billings view displays billings after it has been chosen, by what to sort them.
"""


def all_billings(request, order_by="date"):
    if request.user.is_authenticated:
        context_dic = {}
        billings = Billing.objects.all()

        if order_by == "date":
            context_dic["billings"] = billings.order_by('-date')
        if order_by == "project":
            context_dic["billings"] = billings.order_by('project')
        if order_by == "worker":
            context_dic["billings"] = billings.order_by('worker')

        return render(request, 'databank_system/all_billings.html', context_dic)
    else:
        return redirect(reverse('databank_system:user_login'))


"""
    Users view displays list of all non-admin users, with the option to delete them.
"""


def users(request):
    if request.user.is_authenticated:
        context_dic = {}
        users = User.objects.filter(is_staff=False).order_by('username')
        print(users)
        context_dic["users"] = users
        return render(request, 'databank_system/users.html', context_dic)
    else:
        return redirect(reverse('databank_system:user_login'))


"""
    New billing view displays page with form that allows users to create new instances of billing model.
"""


def new_billing(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BillingForm(request.POST)

            if form.is_valid():
                billing_object = form.save(commit=False)
                billing_object.save()
                return redirect('databank_system:all_billings', 'date')

        return render(request, 'databank_system/new_billing.html', )
    else:
        return redirect(reverse('databank_system:user_login'))


"""
    Single billing view displays page with chosen billing and all its details, 
    additionally with 'edit', 'delete' and 'export' buttons. Export button calls the export_billing view.
"""


def single_billing(request, id):
    if request.user.is_authenticated:
        context_dic = {}
        try:
            context_dic['billing'] = Billing.objects.get(id=id)

        except Billing.DoesNotExist:
            context_dic['billing'] = None
        return render(request, 'databank_system/single_billing.html', context_dic)
    else:
        return redirect(reverse('databank_system:user_login'))


"""
    Delete billing view deletes a chosen instance of billing model.
"""


def delete_billing(request, id):
    if request.user.is_authenticated:
        Billing.objects.filter(id=id).delete()
        return redirect('databank_system:all_billings', 'date')
    else:
        return redirect(reverse('databank_system:user_login'))


"""
    Delete user view deletes a chosen instance of user model.
"""


def delete_user(request, username):
    if request.user.is_authenticated:
        User.objects.filter(username=username).delete()
        return redirect('databank_system:users')
    else:
        return redirect(reverse('databank_system:user_login'))


"""
    Single billing edit view allows user to adjust details of particular chosen billing.
"""


def single_billing_edit(request, id):
    if request.user.is_authenticated:
        context_dic = {}
        try:
            current_billing = Billing.objects.get(id=id)
            context_dic["billing"] = current_billing
            print(current_billing.date)
        except Billing.DoesNotExist:
            context_dic['billing'] = None
        if request.method == 'POST':
            billing_form = BillingUpdateForm(request.POST)
            if billing_form.is_valid():
                current_billing.date = request.POST["date"]
                current_billing.worker = request.POST["worker"]
                current_billing.budget_code = request.POST["budget_code"]
                current_billing.project = request.POST["project"]
                current_billing.unit = request.POST["unit"]
                current_billing.cost = request.POST["cost"]

                current_billing.save()

                context_dic['billing'] = Billing.objects.get(id=id)

                return render(request, 'databank_system/single_billing.html', context_dic)

        return render(request, 'databank_system/single_billing_edit.html', context_dic)
    else:
        return redirect(reverse('databank_system:user_login'))


"""
    Single record edit view allows user to adjust details of particular chosen record.
"""


def single_record_edit(request, id):
    if request.user.is_authenticated:
        context_dic = {}
        try:
            current_record = Record.objects.get(id=id)
            context_dic["record"] = current_record
        except Record.DoesNotExist:
            context_dic['record'] = None
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

                context_dic['record'] = Record.objects.get(id=id)

                return render(request, 'databank_system/single_record.html', context_dic)

        return render(request, 'databank_system/single_record_edit.html', context_dic)
    else:
        return redirect(reverse('databank_system:user_login'))


"""
    Registration view allows already existing users to create new ones.
"""


def registration(request, username_already_exists=False):
    if request.user.is_authenticated:
        context_dic = {}
        context_dic['username_already_exists'] = username_already_exists
        if request.method == 'POST':
            new_user = UserForm(request.POST)
            if new_user.is_valid():
                user = new_user.save()
                user.set_password(user.password)
                user.save()
                return redirect('/')
            else:
                username = request.POST.get('username')
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    user = None
                # if username already exists, pop up error message
                if user is not None:
                    context_dic['username_already_exists'] = True
        else:
            user_form = UserForm()
            context_dic['user_form'] = user_form

        return render(request, 'databank_system/registration.html', context_dic)

    else:
        return redirect(reverse('databank_system:user_login'))


"""
    Login view lets authorised users to log in.
"""


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


"""
    Export billing view creates a csv file named Billing_id where id is the actual id of the billing, filled with
    details of particular billing being exported.
"""


def export_billing(request, id):
    if request.user.is_authenticated:
        response = HttpResponse(content_type='text/csv')
        # generate a csv file
        response['Content-Disposition'] = 'attachment; filename="Billing_' + id + '.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID', 'Date', 'Worker', 'Budget Code', 'Project number', 'Unit', 'Cost'])

        # find chosen billing amongst all billings and write details to the csv file
        billings = Billing.objects.all().values_list('id', 'date', 'worker', 'budget_code', 'project', 'unit', 'cost')
        for billing in billings:
            if str(billing[0]) == id:
                date_string = billing[1].strftime('%d/%m/%Y')
                billing = list(billing)
                billing[1] = date_string
                billing = tuple(billing)
                writer.writerow(billing)

        return response
    else:
        return redirect(reverse('databank_system:user_login'))


"""
    Logout view lets authorised users to log out of the application.
"""


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('databank_system:user_login'))
