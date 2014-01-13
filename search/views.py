from django.shortcuts import render,get_object_or_404,redirect,render_to_response
from django.template import Context,loader
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from django import forms
from search.models import EmployeeDetails

def search(request):
	employees = EmployeeDetails.objects.all()

	if request.method == 'POST':
		key_id = request.POST['key_id']

		if key_id != '':
			employees = employees.filter(emp_id__contains=key_id)

	employees = employees.order_by('emp_id')[:100]

	context = {'employees' : employees}
	return render(request,'search/index.html', context)
