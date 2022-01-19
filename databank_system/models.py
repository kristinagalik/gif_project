from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class NewBilling(models.Model):
    id = models.AutoField(primary_key=True)
    Date = models.CharField(null=True, blank=True, max_length=50)
    Worker = models.CharField(null=True, blank=True, max_length=50)
    BudgetCode = models.CharField(null=True, blank=True, max_length=50)
    Project = models.CharField(null=True, blank=True, max_length=50)
    Unit = models.CharField(null=True, blank=True, max_length=50)
    Cost = models.CharField(null=True, blank=True, max_length=50)

    def save(self, *args, **kwargs):
        super(NewBilling, self).save(*args, **kwargs)

    def _str_(self):
        return self.Project


class NewRecord(models.Model):
    id = models.AutoField(primary_key=True)
    Date = models.CharField(null=True, blank=True, max_length=50)
    Worker = models.CharField(null=True, blank=True, max_length=50)
    Project = models.CharField(null=True, blank=True, max_length=50)
    BudgetCode = models.CharField(null=True, blank=True, max_length=50)
    Email = models.CharField(null=True, blank=True, max_length=50)
    ContactTelNo = models.CharField(null=True, blank=True, max_length=50)
    Procedure = models.CharField(null=True, blank=True, max_length=100)
    ChemicalFixation = models.CharField(null=True, blank=True, max_length=50)
    Negstaining = models.CharField(null=True, blank=True, max_length=50)
    Cryofixation = models.CharField(null=True, blank=True, max_length=50)
    TEMembeddingSchedule = models.CharField(null=True, blank=True, max_length=50)
    SEM = models.CharField(null=True, blank=True, max_length=50)
    Dehydration = models.CharField(null=True, blank=True, max_length=50)
    SEMMount = models.CharField(null=True, blank=True, max_length=50)
    FD = models.CharField(null=True, blank=True, max_length=50)
    CPD = models.CharField(null=True, blank=True, max_length=50)
    Resin = models.CharField(null=True, blank=True, max_length=50)
    SEMCost = models.CharField(null=True, blank=True, max_length=50)
    TempTime = models.CharField(null=True, blank=True, max_length=50)
    Immunolabeling = models.CharField(null=True, blank=True, max_length=50)
    AbDilutionTime = models.CharField(null=True, blank=True, max_length=50)
    AbGoldDilutionTime = models.CharField(null=True, blank=True, max_length=50)
    ContrastStaining = models.CharField(null=True, blank=True, max_length=50)
    Comment = models.CharField(null=True, blank=True, max_length=1000)

    def save(self, *args, **kwargs):
        super(NewRecord, self).save(*args, **kwargs)

    def _str_(self):
        return self.BudgetCode


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True, blank=False, primary_key=True)
    email = models.CharField(max_length=50, unique=True, blank=False)

    def _str_(self):
        return self.user.username
