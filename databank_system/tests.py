from databank_system.models import Billing, Record
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test import TestCase, Client


class BillingTestCase(TestCase):
    def setUp(self):
        self.b1 = Billing.objects.create(date='2018-04-15', worker='worker1', budget_code='budget_code1',
                                         project=1, unit='unit1', cost='cost1')
        self.b1.save()
        self.b2 = Billing.objects.create(date='2017-03-01', worker='worker2', budget_code='budget_code2',
                                         project=13, unit='unit2', cost='cost2')
        self.b2.save()
        self.b3 = Billing.objects.create(worker='', budget_code='', project=3, unit='', cost='')
        self.b3.save()

    def tearDown(self):
        self.b1.delete()
        self.b2.delete()
        self.b3.delete()

    def test_billings_exist(self):
        self.assertEqual(3, Billing.objects.count())

    def test_b1_date_after_b2(self):
        self.assertGreater(self.b1.date, self.b2.date)

    def test_id_not_negative(self):
        self.assertTrue(self.b1.id >= 0)


class RecordTestCase(TestCase):
    def setUp(self):
        self.r1 = Record.objects.create(date='2017-04-15', worker='worker1', procedure='procedure123')
        self.r1.save()
        self.r2 = Record.objects.create(date='2017-03-01', worker='worker2', chemical_fixation='chemical_fixation345',
                                        temp_time='14h 3s')
        self.r2.save()
        self.r3 = Record.objects.create(date='2017-03-01', worker='worker3', procedure='procedure3', temp_time='14h 3s')
        self.r3.save()

    def tearDown(self):
        self.r1.delete()
        self.r2.delete()
        self.r3.delete()

    def test_records_exist(self):
        self.assertEqual(3, Record.objects.count())

    def test_r1_date_after_r2(self):
        self.assertGreater(self.r1.date, self.r2.date)

    def test_r2_date_same_r3(self):
        self.assertEqual(self.r3.date, self.r2.date)


class UserTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='john', email='john@gmail123.com')
        self.user1.set_password("secret_password")
        self.user1.save()
        self.user2 = User.objects.create(username='alice', email='alice@gmail123.com')
        self.user2.set_password("cat12345")
        self.user2.save()
        self.user3 = User.objects.create(username='test', email='test@gmail123.com')
        self.user3.set_password("testtest")
        self.user3.save()

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.user3.delete()

    def test_users_exist(self):
        self.assertEqual(3, User.objects.count())

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_correct(self):
        user = authenticate(username='test', password='testtest')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_user_login(self):
        c = Client()
        logged_in = c.login(username='john', password='secret_password')
        self.assertTrue(logged_in)

        logged_in = c.login(username='nonexisting', password='12345')
        self.assertFalse(logged_in)


class LogInViewTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='john', email='john@gmail123.com')
        self.user1.set_password("secret_password")
        self.user1.save()

    def tearDown(self):
        self.user1.delete()

    def test_correct(self):
        response = self.client.post('/login/', {'username': 'john', 'password': 'secret_password'})
        self.assertRedirects(response, '/')

    def test_wrong_username(self):
        response = self.client.post('/login/', {'username': 'wrong', 'password': 'secret_password'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Account details incorrect.')

    def test_wrong_password(self):
        response = self.client.post('/login/', {'username': 'john', 'password': 'wrong'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Account details incorrect.')


class LogOutTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='john', email='john@gmail123.com')
        self.user1.set_password("secret_password")
        self.user1.save()

    def tearDown(self):
        self.user1.delete()

    def test_log_out(self):
        self.client.login(username='john', password="secret_password")
        response = self.client.get('/all_billings/date/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        response = self.client.get('/all_billings/date/')
        self.assertEqual(response.status_code, 302)


class AllBillingsViewTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='john', email='john@gmail123.com')
        self.user1.set_password("secret_password")
        self.user1.save()
        self.client.login(username='john', password='secret_password')

    def tearDown(self):
        self.user1.delete()

    def test_view_url_exists_empty(self):
        response = self.client.get('/all_billings/date/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['billings'].count(), 0)

    def test_view_url_exists_not_empty(self):
        self.b1 = Billing.objects.create(date='2018-04-15', worker='worker1', budget_code='budget_code1',
                                         project=432, unit='unit1', cost='cost1')
        self.b1.save()
        self.b2 = Billing.objects.create(date='2017-03-01', worker='worker2', budget_code='budget_code2',
                                         project=32423, unit='unit2', cost='cost2')
        self.b2.save()
        self.b3 = Billing.objects.create(worker='', budget_code='', project=100, unit='', cost='')
        self.b3.save()

        response = self.client.get('/all_billings/date/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['billings'].count(), 3)

        self.b1.delete()
        self.b2.delete()
        self.b3.delete()


class AllRecordsViewTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='john', email='john@gmail123.com')
        self.user1.set_password("secret_password")
        self.user1.save()
        self.client.login(username='john', password='secret_password')

    def tearDown(self):
        self.user1.delete()

    def test_view_url_exists_empty(self):
        response = self.client.get('/all_records/date/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['records'].count(), 0)

    def test_view_url_exists_not_empty(self):
        self.r1 = Record.objects.create(date='2017-04-15', worker='worker1', procedure='procedure123')
        self.r1.save()
        self.r2 = Record.objects.create(date='2017-03-01', worker='worker2', chemical_fixation='chemical_fixation345',
                                        temp_time='14h 3s')
        self.r2.save()
        self.r3 = Record.objects.create(date='2017-03-01', worker='worker3', procedure='procedure3', temp_time='14h 3s')
        self.r3.save()

        response = self.client.get('/all_records/date/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['records'].count(), 3)

        self.r1.delete()
        self.r2.delete()
        self.r3.delete()


class RedirectTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='john', email='john@gmail123.com')
        self.user1.set_password("secret_password")
        self.user1.save()

    def tearDown(self):
        self.user1.delete()

    def test_redirect_not_logged_in_homepage(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_redirect_logged_in_homepage(self):
        self.client.login(username='john', password='secret_password')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_not_logged_in_all_records(self):
        response = self.client.get('/all_records/date/')
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_redirect_logged_in_all_records(self):
        self.client.login(username='john', password='secret_password')
        response = self.client.get('/all_records/date/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_not_logged_in_new_record(self):
        response = self.client.get('/new_record/')
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_redirect_logged_in_new_record(self):
        self.client.login(username='john', password='secret_password')
        response = self.client.get('/new_record/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_not_logged_in_all_billings(self):
        response = self.client.get('/all_billings/date/')
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_redirect_logged_in_all_billings(self):
        self.client.login(username='john', password='secret_password')
        response = self.client.get('/all_billings/date/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_not_logged_in_new_billing(self):
        response = self.client.get('/new_billing/')
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_redirect_logged_in_new_billing(self):
        self.client.login(username='john', password='secret_password')
        response = self.client.get('/new_billing/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_not_logged_in_register(self):
        response = self.client.get('/registration/')
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_redirect_logged_in_register(self):
        self.client.login(username='john', password='secret_password')
        response = self.client.get('/registration/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_not_logged_in_single_record_edit(self):
        response = self.client.get('/single_record_edit/1/')
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_redirect_logged_in_single_record_edit(self):
        self.client.login(username='john', password='secret_password')
        response = self.client.get('/single_record_edit/1/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_not_logged_in_single_billing_edit(self):
        response = self.client.get('/single_billing_edit/1/')
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_redirect_logged_in_single_billing_edit(self):
        self.client.login(username='john', password='secret_password')
        response = self.client.get('/single_billing_edit/1/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_not_logged_in_single_record(self):
        response = self.client.get('/single_record/1/')
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_redirect_logged_in_single_record(self):
        self.client.login(username='john', password='secret_password')
        response = self.client.get('/single_record/1/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_not_logged_in_single_billing(self):
        response = self.client.get('/single_billing/5/')
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_redirect_logged_in_single_billing(self):
        self.client.login(username='john', password='secret_password')
        response = self.client.get('/single_billing/5/')
        self.assertEqual(response.status_code, 200)


class CreateBillingTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='john', email='john@gmail123.com')
        self.user1.set_password("secret_password")
        self.user1.save()
        self.client.login(username='john', password='secret_password')

    def tearDown(self):
        self.user1.delete()

    def test_create_object(self):
        response = self.client.post('/new_billing/', {'date': '2022-03-12', 'worker': 'melanie', 'budget_code': '123'})
        self.assertEqual(Billing.objects.count(), 1)
        self.assertRedirects(response, '/all_billings/date/')

    def test_create_object_fails(self):
        response = self.client.post('/new_billing/', {'date': '20222-03-12', 'worker': 'melanie', 'budget_code': '123'})
        self.assertEqual(Billing.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'databank_system/new_billing.html')


class CreateRecordTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='john', email='john@gmail123.com')
        self.user1.set_password("secret_password")
        self.user1.save()
        self.client.login(username='john', password='secret_password')

    def tearDown(self):
        self.user1.delete()

    def test_create_object(self):
        response = self.client.post('/new_record/', {'date': '2022-03-12', 'worker': 'john', 'budget_code': '123'})
        self.assertEqual(Record.objects.count(), 1)
        self.assertRedirects(response, '/all_records/date/')

    def test_create_object_fails(self):
        response = self.client.post('/new_record/',
                                    {'date': '20222-03-12', 'worker': 'john', 'budget_code': '123', 'procedure': 'xyz'})
        self.assertEqual(Record.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'databank_system/new_record.html')
