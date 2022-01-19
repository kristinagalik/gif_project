import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gif_project.settings')
import django

django.setup()
from databank_system.models import NewRecord, NewBilling
from django.contrib.auth.models import User


def generate_data():
    # generate users
    users = [
        {'username': 'user1', 'email': 'user1@gmail.com'},
        {'username': 'user2', 'email': 'user2@gmail.com'},
        {'username': 'user3', 'email': 'user3@gmail.com'},
        {'username': 'user4', 'email': 'user4@gmail.com'},
        {'username': 'user5', 'email': 'user5@gmail.com'},
        {'username': 'user6', 'email': 'user6@gmail.com'}
    ]

    for item in users:
        add_user(item["username"], item["email"])

    # generate billings

    billings = [
        {'date': '15.04.2018', 'worker': 'John P.', 'budget_code': '121', 'project': '1123', 'unit': '23',
         'cost': '15'},
        {'date': '01.09.2019', 'worker': 'Elise A.', 'budget_code': '122', 'project': '1231', 'unit': '23243',
         'cost': '543.5'},
        {'date': '28.08.2020', 'worker': 'Barry H.', 'budget_code': '123', 'project': '3121', 'unit': '2323',
         'cost': '0.55'},
        {'date': '15.04.2018', 'worker': 'John P.', 'budget_code': '124', 'project': '1543', 'unit': '23324',
         'cost': '543'},
        {'date': '14.04.2019', 'worker': 'John P.', 'budget_code': '125', 'project': '172343', 'unit': '27653',
         'cost': '15.88'},
        {'date': '01.09.2021', 'worker': 'Sophie M.', 'budget_code': '126', 'project': '153', 'unit': '2384',
         'cost': '943.3'},
    ]

    for item in billings:
        add_billing(item["date"], item["worker"], item["budget_code"], item["project"], item["unit"], item["cost"])

    # generate records

    records = [
        {'date': '11.4.2015', 'worker': 'Barry H.', 'project': '123', 'budget_code': '321', 'email': 'barry_h@gmail.com',
         'contact_tel_no': '2834928342', 'procedure': 'Type A', 'chemical_fixation': 'Yes', 'negstaining': 'Maybe',
         'cryofixation': 'Non applicable', 'tem_embedding_schedule': 'No', 'sem': 'Dont know this one at all',
         'dehydration': 'there was nothing to dehydrate', 'sem_mount': '7', 'fd': 'OO', 'cpd': 'EE', 'resin': '17%',
         'sem_cost': '£13', 'temp_time': '13 seconds', 'immunolabeling': 'No', 'ab_dilution_time': 'ABC',
         'ab_gold_dilution_time': 'No', 'contrast_staining': '14', 'comment': 'Nothing to comment on'},
        {'date': '14.5.2019', 'worker': 'Anna J.', 'project': '324', 'budget_code': '234', 'email': 'anna_j@gmail.com',
         'contact_tel_no': '0212345678', 'procedure': 'Type C', 'chemical_fixation': 'No', 'negstaining': 'No',
         'cryofixation': 'Yes', 'tem_embedding_schedule': 'No', 'sem': '0.5',
         'dehydration': 'there was nothing to dehydrate', 'sem_mount': '7', 'fd': 'OO', 'cpd': 'EE', 'resin': '17%',
         'sem_cost': '0.5', 'temp_time': '12', 'immunolabeling': 'Yes', 'ab_dilution_time': 'ABC',
         'ab_gold_dilution_time': 'No', 'contrast_staining': '0', 'comment': 'Nothing to comment on'},
        {'date': '1.5.2021', 'worker': 'Barry H.', 'project': '2342', 'budget_code': '68', 'email': 'barry_h@gmail.com',
         'contact_tel_no': '2834928342', 'procedure': 'Type D', 'chemical_fixation': 'Yes', 'negstaining': 'Yes',
         'cryofixation': 'Non applicable', 'tem_embedding_schedule': 'Yes', 'sem': 'ABC',
         'dehydration': 'there was nothing to dehydrate', 'sem_mount': '7', 'fd': 'OO', 'cpd': 'EE', 'resin': '17%',
         'sem_cost': 'ABC', 'temp_time': '123', 'immunolabeling': 'No', 'ab_dilution_time': 'ABC',
         'ab_gold_dilution_time': 'No', 'contrast_staining': '', 'comment': 'Nothing to comment on'},
    ]

    for item in records:
        add_record(item["date"], item["worker"], item["project"], item["budget_code"], item["email"], item["contact_tel_no"],
                   item["procedure"], item["chemical_fixation"], item["negstaining"], item["cryofixation"], item["tem_embedding_schedule"], item["sem"],
                   item["dehydration"], item["sem_mount"], item["fd"], item["cpd"], item["resin"], item["sem_cost"], item["temp_time"],
                   item["immunolabeling"], item["ab_dilution_time"], item["ab_gold_dilution_time"], item["contrast_staining"], item["comment"],)


def add_user(username, email):
    u = User.objects.get_or_create(username=username)[0]
    u.email = email
    u.save()
    return u


def add_billing(date, worker, budget_code, project, unit, cost):
    b = NewBilling.objects.get_or_create(Date=date, Worker=worker, BudgetCode=budget_code, Project=project, Unit=unit,
                                         Cost=cost)[0]
    b.save()
    return b


def add_record(date, worker, project, budget_code, email, contact_tel_no, procedure, chemical_fixation, negstaining,
               cryofixation, tem_embedding_schedule, sem, dehydration, sem_mount, fd, cpd, resin, sem_cost, temp_time,
               immunolabeling, ab_dilution_time, ab_gold_dilution_time, contrast_staining, comment):
    r = NewRecord.objects.get_or_create(Date=date, Worker=worker, Project=project, BudgetCode=budget_code, Email=email,
                                        ContactTelNo=contact_tel_no, Procedure=procedure,
                                        ChemicalFixation=chemical_fixation, Negstaining=negstaining,
                                        Cryofixation=cryofixation, TEMembeddingSchedule=tem_embedding_schedule,
                                        SEM=sem, Dehydration=dehydration,
                                        SEMMount=sem_mount, FD=fd, CPD=cpd, Resin=resin, SEMCost=sem_cost,
                                        TempTime=temp_time, Immunolabeling=immunolabeling,
                                        AbDilutionTime=ab_dilution_time, AbGoldDilutionTime=ab_gold_dilution_time,
                                        ContrastStaining=contrast_staining, Comment=comment)[0]
    r.save()
    return r


if __name__ == '__main__':
    print('Starting population script...')
    generate_data()
