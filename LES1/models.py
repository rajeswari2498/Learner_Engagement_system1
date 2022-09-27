from django.db import models

# Create your models here.
class UserData(models.Model):
    first_name = models.CharField(max_length = 12)
    last_name = models.CharField(max_length= 12)
    date_of_birth = models.DateField()
    email_id = models.EmailField()
    password = models.CharField(max_length=12)
    re_password = models.CharField(max_length = 12)

    def __str__(self):
        return f'{self.first_name}, { self.email_id}, {self.password}'

