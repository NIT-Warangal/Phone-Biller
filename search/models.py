from django.db import models

class EmployeeDetails(models.Model):
	emp_id = models.CharField(max_length=10)
	emp_name = models.CharField(max_length=50)
	emp_phone = models.CharField(max_length=15) # CUG 99
	emp_bill = models.CharField(max_length=10)  # CUG 99 Bill
	emp_email = models.CharField(max_length=50)
	emp_intercom = models.CharField(max_length=10) # Intercom number
	emp_phoneofficial = models.CharField(max_length=15) # CUG Official
	emp_intercombill = models.CharField(max_length=10)  # Intercom Bill.
	emp_phoneofficialbill = models.CharField(max_length=10) # CUG Official Bill.
	emp_total = models.CharField(max_length=50) # Total = CUG99 Bill + CUG Official Bill+ Intercom Bill


	def __unicode__(self):
		return self.emp_name
