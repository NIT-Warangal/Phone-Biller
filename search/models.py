from django.db import models

class EmployeeDetails(models.Model):
	emp_id = models.CharField(max_length=10)
	emp_name = models.CharField(max_length=50)
	emp_phone = models.CharField(max_length=15)
	emp_bill = models.CharField(max_length=10)
	emp_email = models.CharField(max_length=50)

	def __unicode__(self):
		return self.emp_name
