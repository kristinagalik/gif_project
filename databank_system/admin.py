from django.contrib import admin
from databank_system.models import UserInfo, NewBilling, NewRecord


admin.site.register(UserInfo)


class NewBillingAdmin(admin.ModelAdmin):
    list_display = ('Date', 'Worker', 'BudgetCode', 'Project', 'Unit', 'Cost')


admin.site.register(NewBilling, NewBillingAdmin)


class NewRecordAdmin(admin.ModelAdmin):
    list_display = ('Date', 'Worker', 'Project', 'BudgetCode', 'Email', 'ContactTelNo', 'Procedure', 'ChemicalFixation',
                    'Negstaining', 'Cryofixation', 'TEMembeddingSchedule', 'SEM', 'Dehydration', 'SEMMount', 'FD', 'CPD',
                    'Resin', 'SEMCost', 'TempTime', 'Immunolabeling', 'AbDilutionTime', 'AbGoldDilutionTime',
                    'ContrastStaining', 'Comment')


admin.site.register(NewRecord, NewRecordAdmin)
