from django.db import models
from datetime import date
from django.utils import timezone
from django.core.validators import MaxValueValidator
# Create your models here.

class Target(models.Model):
    text = models.CharField(max_length=50, verbose_name='text')
    time_to_beat = models.TimeField(verbose_name='when it should be done,')
    day_to_beat = models.DateField(default=date.today(), verbose_name='on what day need to be maden?')
    important = models.IntegerField(default=0, validators=[MaxValueValidator(3)], verbose_name='how important the goal is (from 0 to 3)')
    is_done = models.BooleanField(default=0, verbose_name='made?')
    is_great = models.BooleanField(default=0, verbose_name='long-term goal?')
    is_repeat = models.BooleanField(default=0, verbose_name='repeatable goal?')
    repeat_every = models.IntegerField(default=0, verbose_name='repeat every')
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.text
    def publish(self):
        self.pub_date = timezone.now()
        self.save()