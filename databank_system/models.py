from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Billing(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(null=True, blank=True)
    worker = models.CharField(null=True, blank=True, max_length=50)
    budget_code = models.CharField(null=True, blank=True, max_length=50)
    project = models.CharField(null=True, blank=True, max_length=50)
    unit = models.CharField(null=True, blank=True, max_length=50)
    cost = models.CharField(null=True, blank=True, max_length=50)

    def save(self, *args, **kwargs):
        super(Billing, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


class Record(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(null=True, blank=True)
    worker = models.CharField(null=True, blank=True, max_length=50)
    project = models.CharField(null=True, blank=True, max_length=50)
    budget_code = models.CharField(null=True, blank=True, max_length=50)
    email = models.CharField(null=True, blank=True, max_length=50)
    contact_tel_no = models.CharField(null=True, blank=True, max_length=50)
    procedure = models.CharField(null=True, blank=True, max_length=100)
    chemical_fixation = models.CharField(null=True, blank=True, max_length=50)
    negstaining = models.CharField(null=True, blank=True, max_length=50)
    cryofixation = models.CharField(null=True, blank=True, max_length=50)
    tem_embedding_schedule = models.CharField(null=True, blank=True, max_length=50)
    sem = models.CharField(null=True, blank=True, max_length=50)
    dehydration = models.CharField(null=True, blank=True, max_length=50)
    sem_mount = models.CharField(null=True, blank=True, max_length=50)
    fd = models.CharField(null=True, blank=True, max_length=50)
    cpd = models.CharField(null=True, blank=True, max_length=50)
    resin = models.CharField(null=True, blank=True, max_length=50)
    sem_cost = models.CharField(null=True, blank=True, max_length=50)
    temp_time = models.CharField(null=True, blank=True, max_length=50)
    immunolabeling = models.CharField(null=True, blank=True, max_length=50)
    ab_dilution_time = models.CharField(null=True, blank=True, max_length=50)
    ab_gold_dilution_time = models.CharField(null=True, blank=True, max_length=50)
    contrast_staining = models.CharField(null=True, blank=True, max_length=50)
    comment = models.CharField(null=True, blank=True, max_length=1000)

    def save(self, *args, **kwargs):
        super(Record, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True, blank=False, primary_key=True)
    email = models.CharField(max_length=50, unique=True, blank=False)

    def __str__(self):
        return self.user.username
