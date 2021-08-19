from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import * 
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
import csv
# Create your views here.

def resource_view(request):
	resource_object=Resources.objects.all()
	function_object=Functions.objects.all()
	context={'resource_object':resource_object, 'function_object':function_object}
	return render(request,'Home/dashboard.html',context)

def admin_view(request):
	resource_object=Resources.objects.all()
	function_object=Functions.objects.all()
	users_object=Users.objects.all()
	#resource filter
	resourcemyfilter=ResourceFilter(request.GET, queryset=resource_object)
	resource_object=resourcemyfilter.qs
	#user filter
	usermyfilter=UserFilter(request.GET, queryset=users_object)
	users_object=usermyfilter.qs
	context={'resource_object':resource_object, 'function_object':function_object,
	'users_object':users_object,'resourcemyfilter':resourcemyfilter,'usermyfilter':usermyfilter}
	return render(request,'Home/admin_page.html',context)

# def users_view(request):
# 	resource_object=Users.objects.all()
# 	function_object=Functions.objects.all()
# 	context={'resource_object':resource_object, 'function_object':function_object}
# 	return render(request,'Home/admin_page.html',context)

# def function_view(request):
# 	resources=Functions.objects.all()
# 	context={'functions':resources}
# 	return render(request,'Home/dashboard.html',context)

	
	# accounts=Accounts.objects.all()
	# context={'accounts':accounts}
	# return render(request,'Home/dashboard.html',context)

def FTE_plan_func(request):
	# resource_object=Resources.objects.all()
	# function_object=Functions.objects.all()
	labor_allocat_object=LaborAllocations.objects.filter(quarter__in =['q419','q120','q220','q320','q420','q121','q221'])
	quarter_filter=labor_allocat_object.values('quarter').distinct()
	amount_filter=labor_allocat_object.values('amount')
	resource_filter=labor_allocat_object.values('resource_num','project_num')
	print(resource_filter)
	# projects_object=Projects.objects.all()
	# filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['activity']
	context={ 'labor_allocat_object':labor_allocat_object,'quarter_filter':quarter_filter,
			  'amount_filter':amount_filter,'resource_filter':resource_filter}
	return render(request,'Home/FTE_Plan.html',context)

def Project_SLA_func(request):
	resource_object=Resources.objects.all()
	function_object=Functions.objects.all()
	context={'resource_object':resource_object, 'function_object':function_object}
	return render(request,'Home/Project_SLA.html',context)

def Program_SLA_func(request):
	resource_object=Resources.objects.all()
	function_object=Functions.objects.all()
	context={'resource_object':resource_object, 'function_object':function_object}
	return render(request,'Home/Program_SLA.html',context)


# def projectADD_func(request):
# 	form=ProjectADD()
# 	if request.method == 'POST':
# 		print('Printing POST:', request.POST)
# 		form = ProjectADD(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			print('Printing POST after formvalid:', request.POST)
# 			return redirect('/Admin')

# 	context = {'form':form}
# 	print('Printing POST after context:', form.fields)
# 	return render(request, 'Home/adminresource_form.html', context)
def projectADD_func(request):
	form = ProjectADD()
	if request.method == 'POST':
		print('Printing POST:', request.POST)
		form = ProjectADD(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/Admin')

	context = {'form':form}
	return render(request, 'Home/adminresource_form.html', context)


def programADD_func(request):
	form = ProgramADD()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = ProgramADD(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/Admin')

	context = {'form':form}
	return render(request, 'Home/adminresource_form.html', context)


def createadmin_resource(request):
	form = AdminResource()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = AdminResource(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/Admin')

	context = {'form':form}
	return render(request, 'Home/adminresource_form.html', context)

def createadmin_user(request):
	form = AdminUser()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = AdminUser(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/Admin')

	context = {'form':form}
	return render(request, 'Home/adminresource_form.html', context)

def resourceUpdate(request,pk):
	resource_object=Resources.objects.get(resource_num=pk)
	form=AdminResource(instance=resource_object)
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = AdminResource(request.POST,instance=resource_object)
		if form.is_valid():
			form.save()
			return redirect('/Admin')
	context={'form':form}
	return render(request, 'Home/adminresource_form.html', context)

def resourceDelete(request,pk):
	resource_object=Resources.objects.get(resource_num=pk)
	if request.method=='POST':
		resource_object.delete()
		return redirect('/Admin')
	context={'item': resource_object}
	return render(request, 'Home/resource_delete.html', context)

def userUpdate(request,pk):
	user_object=Users.objects.get(id=pk)
	form=AdminUser(instance=user_object)
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = AdminUser(request.POST,instance=user_object)
		if form.is_valid():
			form.save()
			return redirect('/Admin')
	context={'form':form}
	return render(request, 'Home/adminresource_form.html', context)

def userDelete(request,pk):
	user_object=Users.objects.get(id=pk)
	if request.method=='POST':
		user_object.delete()
		return redirect('/Admin')
	context={'item': user_object}
	return render(request, 'Home/user_delete.html', context)

def contractorTracker_view(request):
	contractorTrackerobject=ContractorTracker.objects.all()
	#contractor filter
	contractormyfilter=ContractorFilter(request.GET, queryset=contractorTrackerobject)
	contractorTrackerobject=contractormyfilter.qs
	context={'contractorTrackerobject':contractorTrackerobject,
	'contractormyfilter':contractormyfilter}
	return render(request,'Home/Contractor_Tracker.html',context)

def contractorADD(request):
	form = ContractorTrackerADD()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = ContractorTrackerADD(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/ContractorTracker')

	context = {'form':form}
	return render(request, 'Home/contract_tracker_form.html', context)

def contractorUpdate(request,pk):
	tracker_object=ContractorTracker.objects.get(name=pk)
	form=ContractorTrackerADD(instance=tracker_object)
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = ContractorTrackerADD(request.POST,instance=tracker_object)
		if form.is_valid():
			form.save()
			return redirect('/ContractorTracker')
	context={'form':form}
	return render(request, 'Home/adminresource_form.html', context)

def contractorDelete(request,pk):
	tracker_object=ContractorTracker.objects.get(name=pk)
	if request.method=='POST':
		tracker_object.delete()
		return redirect('/ContractorTracker')
	context={'item': tracker_object}
	return render(request, 'Home/contractor_delete.html', context)

def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Name', 'Vendor', 'Geo_id', 'Manager'])

    for member in ContractorTracker.objects.all().values_list('name', 'vendor', 'geo_id', 'manager'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="contractor.csv"'

    return response
