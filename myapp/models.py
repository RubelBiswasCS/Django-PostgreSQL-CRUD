from django.db import models
#from django.utils import timezone

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    #date = models.DateTimeField(default=timezone.now)
    #age = models.IntegerField(max_length=3)
    country = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def age(self):
        import datetime
        return int((datetime.date.today() - self.birthday).days / 365.25  )



