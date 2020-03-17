from django.forms import ModelForm
import datetime

from django.db import models
from django.utils import timezone
from django.forms import ModelForm
# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    function = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='%Y/%m/%d/')
    birthday = models.DateField()

    def __str__(self):
        """Use in django administration app
        """
        return f"{self.first_name}  {self.last_name}"

    def is_date_superior_to_eighteen(self):
        return self.birthday >= datetime.date.today() - datetime.timedelta(days=18)


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
