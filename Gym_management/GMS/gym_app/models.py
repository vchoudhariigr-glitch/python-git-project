from django.db import models
from django.utils import timezone

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    # def __str__(self):
    #     return self.name


class Member(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    join_date = models.DateField(default=timezone.now)
    membership_plan = models.CharField(max_length=50, null=True, blank=True)
    fees_paid = models.BooleanField(default=False)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)

    # def __str__(self):
    #     return self.name