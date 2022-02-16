from django.contrib import admin
from databank_system.models import UserInfo, Billing, Record


admin.site.register(UserInfo)


class BillingAdmin(admin.ModelAdmin):
    list_display = ('date', 'worker', 'budget_code', 'project', 'unit', 'cost')


admin.site.register(Billing, BillingAdmin)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'worker', 'project', 'budget_code', 'email', 'contact_tel_no', 'procedure', 'chemical_fixation',
                    'negstaining', 'cryofixation', 'tem_embedding_schedule', 'sem', 'dehydration', 'sem_mount', 'fd', 'cpd',
                    'resin', 'sem_cost', 'temp_time', 'immunolabeling', 'ab_dilution_time', 'ab_gold_dilution_time',
                    'contrast_staining', 'comment')


admin.site.register(Record, RecordAdmin)
