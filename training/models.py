from django.db import models
from django.contrib.auth.models import User
import datetime

class Drill_types(models.Model):
    drill_type = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Drill types"
        db_table = "training_drill_types"

    def __str__(self):
        return self.drill_type


class Drills(models.Model):
    name = models.CharField(max_length=50)
    drill_type = models.ForeignKey(Drill_types, on_delete=models.CASCADE)
    score_type = models.IntegerField()
    has_test = models.BooleanField()
    time_bound = models.BooleanField()
    test_duration = models.IntegerField()
    active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Drills"
        db_table = "training_drills"

    def __str__(self):
        return self.name


class Training_sessions(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drill = models.ForeignKey(Drills, on_delete=models.CASCADE)
    minutes = models.IntegerField(null=False, blank=False)
    date = models.DateField(default=datetime.date.today, null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Training sessions"
        db_table = "training_sessions"

    def __str__(self):
        return str(self.drill)
