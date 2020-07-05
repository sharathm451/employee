from django.db import models

# Create your models here.
class Emp(models.Model):
    Emp_id=models.CharField(max_length=20)
    Emp_name=models.CharField(max_length=30)
    Emp_salary=models.FloatField()
    class Meta:
        db_table="Emp"