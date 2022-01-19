from django import forms
from databank_system.models import UserInfo, NewRecord, NewBilling
from django.contrib.auth.models import User
from django.utils import timezone


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               label='')

    class Meta:
        model = User
        fields = ('username', 'password')


class NewBillingForm(forms.ModelForm):
    Date = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    Worker = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    BudgetCode = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    Project = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    Unit = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    Cost = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))

    class Meta:
        model = NewBilling
        fields = ('Date', 'Worker', 'BudgetCode', 'Project', 'Unit', 'Cost')


class NewRecordForm(forms.ModelForm):
    Date = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    Worker = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    Project = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    BudgetCode = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    Email = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    ContactTelNo = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    Procedure = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    ChemicalFixation = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    Negstaining = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    Cryofixation = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    TEMembeddingSchedule = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    SEM = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    Dehydration = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    SEMMount = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    FD = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    CPD = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    Resin = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    SEMCost = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    TempTime = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    Immunolabeling = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    AbDilutionTime = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    AbGoldDilutionTime = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    ContrastStaining = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    Comment = forms.CharField(max_length=1000, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))

    class Meta:
        model = NewRecord
        fields = ('Date', 'Worker', 'Project', 'BudgetCode', 'Email', 'ContactTelNo', 'Procedure', 'ChemicalFixation',
                    'Negstaining', 'Cryofixation', 'TEMembeddingSchedule', 'SEM', 'Dehydration', 'SEMMount', 'FD', 'CPD',
                    'Resin', 'SEMCost', 'TempTime', 'Immunolabeling', 'AbDilutionTime', 'AbGoldDilutionTime',
                    'ContrastStaining', 'Comment')
