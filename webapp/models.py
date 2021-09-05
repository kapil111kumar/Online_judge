from django.db import models

# Create your models here.
class Problems(models.Model):
    Pro_name = models.CharField(max_length=200)
    Statement = models.CharField(max_length=2000)
    Code = models.CharField(max_length=4000)
    Difficulty = models.CharField(max_length=100)


class Solutions(models.Model):
    Sol_name = models.ForeignKey(Problems, on_delete=models.CASCADE)
    Verdict = models.CharField(max_length=100)
    Submitted = models.DateTimeField('Time Submitted')


class Testcase(models.Model):
    Tc_name = models.ForeignKey(Problems, on_delete=models.CASCADE)
    Input = models.CharField(max_length=200)
    Output = models.CharField(max_length=200)
