from databank_system.models import Record, Billing
from django.contrib.auth.models import User
from django import forms


"""
    UserForm form creates a User model instance, requesting the username and password of the user
"""


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               label='')

    class Meta:
        model = User
        fields = ('username', 'password')


"""
    BillingForm form creates a Billing model instance, requesting the following fields
"""


class BillingForm(forms.ModelForm):
    date = forms.DateField(required=False)
    worker = forms.CharField(max_length=200, required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    budget_code = forms.CharField(max_length=200, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    project = forms.IntegerField(required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    unit = forms.CharField(max_length=200, required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    cost = forms.CharField(max_length=200, required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))

    class Meta:
        model = Billing
        fields = ('date', 'worker', 'budget_code', 'project', 'unit', 'cost')


"""
    RecordForm form creates a Record model instance, requesting the following fields
"""


class RecordForm(forms.ModelForm):
    date = forms.DateField(required=False)
    worker = forms.CharField(max_length=200, required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    project = forms.IntegerField(required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    budget_code = forms.CharField(max_length=200, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    email = forms.CharField(max_length=200, required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    contact_tel_no = forms.CharField(max_length=200, required=False,
                                     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    procedure = forms.CharField(max_length=200, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    chemical_fixation = forms.CharField(max_length=200, required=False,
                                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    negstaining = forms.CharField(max_length=200, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    cryofixation = forms.CharField(max_length=200, required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    tem_embedding_schedule = forms.CharField(max_length=200, required=False,
                                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    sem = forms.CharField(max_length=200, required=False,
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    dehydration = forms.CharField(max_length=200, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    sem_mount = forms.CharField(max_length=200, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    fd = forms.CharField(max_length=200, required=False,
                         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    cpd = forms.CharField(max_length=200, required=False,
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    resin = forms.CharField(max_length=200, required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    sem_cost = forms.CharField(max_length=200, required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    temp_time = forms.CharField(max_length=200, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    immunolabeling = forms.CharField(max_length=200, required=False,
                                     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    ab_dilution_time = forms.CharField(max_length=200, required=False,
                                       widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    ab_gold_dilution_time = forms.CharField(max_length=200, required=False,
                                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    contrast_staining = forms.CharField(max_length=200, required=False,
                                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    comment = forms.CharField(max_length=5000, required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))

    class Meta:
        model = Record
        fields = (
            'date', 'worker', 'project', 'budget_code', 'email', 'contact_tel_no', 'procedure', 'chemical_fixation',
            'negstaining', 'cryofixation', 'tem_embedding_schedule', 'sem', 'dehydration', 'sem_mount', 'fd', 'cpd',
            'resin', 'sem_cost', 'temp_time', 'immunolabeling', 'ab_dilution_time', 'ab_gold_dilution_time',
            'contrast_staining', 'comment')


"""
    BillingUpdateForm form updates a particular Billing model instance
"""


class BillingUpdateForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ('date', 'worker', 'budget_code', 'project', 'unit', 'cost')


"""
    RecordUpdateForm form updates a particular Record model instance
"""


class RecordUpdateForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = (
            'date', 'worker', 'project', 'budget_code', 'email', 'contact_tel_no', 'procedure', 'chemical_fixation',
            'negstaining', 'cryofixation', 'tem_embedding_schedule', 'sem', 'dehydration', 'sem_mount', 'fd', 'cpd',
            'resin', 'sem_cost', 'temp_time', 'immunolabeling', 'ab_dilution_time', 'ab_gold_dilution_time',
            'contrast_staining', 'comment')
