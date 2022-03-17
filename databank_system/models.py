from django.db import models

"""
    Billing model is made up of: id, date, worker, budget code, project number, unit and cost.
"""


class Billing(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(null=True, blank=True)
    worker = models.CharField(null=True, blank=True, max_length=200)
    budget_code = models.CharField(null=True, blank=True, max_length=200)
    project = models.IntegerField(null=True, blank=True)
    unit = models.CharField(null=True, blank=True, max_length=200)
    cost = models.CharField(null=True, blank=True, max_length=200)

    def save(self, *args, **kwargs):
        super(Billing, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


"""
    Record model is made up of: id, date, worker, project number, budget code, email, contact tel number, 
    type of procedure, chemical fixation, negstaining, cryofixation, tem embedding schedule, SEM, dehydration, SEM mount,
    FD, CPD, resin, SEM cost, temp time, immunolabeling, AB dilution time, AB gold dilution time, contrast staining and 
    comment.
"""


class Record(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(null=True, blank=True)
    worker = models.CharField(null=True, blank=True, max_length=200)
    project = models.IntegerField(null=True, blank=True)
    budget_code = models.CharField(null=True, blank=True, max_length=200)
    email = models.CharField(null=True, blank=True, max_length=200)
    contact_tel_no = models.CharField(null=True, blank=True, max_length=200)
    procedure = models.CharField(null=True, blank=True, max_length=100)
    chemical_fixation = models.CharField(null=True, blank=True, max_length=200)
    negstaining = models.CharField(null=True, blank=True, max_length=200)
    cryofixation = models.CharField(null=True, blank=True, max_length=200)
    tem_embedding_schedule = models.CharField(null=True, blank=True, max_length=200)
    sem = models.CharField(null=True, blank=True, max_length=200)
    dehydration = models.CharField(null=True, blank=True, max_length=200)
    sem_mount = models.CharField(null=True, blank=True, max_length=200)
    fd = models.CharField(null=True, blank=True, max_length=200)
    cpd = models.CharField(null=True, blank=True, max_length=200)
    resin = models.CharField(null=True, blank=True, max_length=200)
    sem_cost = models.CharField(null=True, blank=True, max_length=200)
    temp_time = models.CharField(null=True, blank=True, max_length=200)
    immunolabeling = models.CharField(null=True, blank=True, max_length=200)
    ab_dilution_time = models.CharField(null=True, blank=True, max_length=200)
    ab_gold_dilution_time = models.CharField(null=True, blank=True, max_length=200)
    contrast_staining = models.CharField(null=True, blank=True, max_length=200)
    comment = models.CharField(null=True, blank=True, max_length=5000)

    def save(self, *args, **kwargs):
        super(Record, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
