from django.test import TestCase
from LES1.forms import RegisterForm
from datetime import date
from django.urls import reverse
from  .models import UserData

# Create your tests here.
class RegisterFormTest(TestCase):
    # if passwords Don't Match
    def test_passwords_not_match(self):
        date1 = date(year=2020, month=1, day=31)
        form = RegisterForm(data={'first_name':"Konda","last_name":"spoorthy","date_of_birth": date1, 'email_id':"kondasaispoorthy@gmail.com", 'password':"Konda@74","re_password":"Konda@2000"})
        self.assertFalse(form.is_valid())

    # if age is greater than 20
    def test_date_of_birth(self):
        date2 = date(year = 2000, month=1, day=30)
        form = RegisterForm(data={'first_name':"Konda","last_name":"spoorthy","date_of_birth": date2, 'email_id':"kondasaispoorthy@gmail.com", 'password':"Konda@74","re_password":"Konda@74"})
        self.assertFalse(form.is_valid())

    # if D.O.B and  Passwords match
    def test_twofields(self):
        date3 = date(year = 2010, month=1, day=30)
        form = RegisterForm(data={'first_name':"Konda","last_name":"spoorthy","date_of_birth": date3, 'email_id':"kondasaispoorthy@gmail.com", 'password':"Konda@74","re_password":"Konda@74"})
        self.assertTrue(form.is_valid())

    # checking Error Messages in form
    def test_form_invalid_date_of_birth(self):
        date4 = date(year = 1998, month=1, day=30)
        response = self.client.post(reverse('LES1:register-form'),{'first_name':"Konda","last_name":"spoorthy","date_of_birth": date4, 'email_id':"kondasaispoorthy@gmail.com", 'password':"Konda@74","re_password":"Konda@74"})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'date_of_birth', 'Too old to Register') 

    # Models are  not added if the data is Not Valid
    def test_sample_models(self):
        date5 = date(year = 2000, month=1, day=30)
        response = self.client.post(reverse('LES1:register-form'),{'first_name':"Konda","last_name":"spoorthy","date_of_birth": date5, 'email_id':"kondasaispoorthy@gmail.com", 'password':"Konda@74","re_password":"Konda@74"})
        self.assertEqual(UserData.objects.all().count(),0)

    # Model is added to DB if the data is valid
    def test_checking_models(self):
        date6 = date(year = 2010, month=1, day=30)
        response = self.client.post(reverse('LES1:register-form'),{'first_name':"Konda","last_name":"spoorthy","date_of_birth": date6, 'email_id':"kondasaispoorthy@gmail.com", 'password':"Konda@74","re_password":"Konda@74"})
        self.assertEqual(UserData.objects.all().count(),1)