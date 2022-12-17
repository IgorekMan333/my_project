from django.db import models


class Employees(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    salary = models.IntegerField()
    reports_to = models.ForeignKey('self', models.DO_NOTHING, db_column='reports_to', blank=True, null=True)
    office = models.ForeignKey('Offices', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employees'


class Offices(models.Model):
    office_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'offices'

    def __str__(self):
        return self.address
