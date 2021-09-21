from django.forms import ModelForm
from .models import *


class LaborAllocationForm(ModelForm):
	class Meta:
		model = LaborAllocations
		fields = 'function_id','resource_num','activity'

class AdminResource(ModelForm):
	class Meta:
		model = Resources
		fields = 'resource','geo','function','active'

class AdminUser(ModelForm):
	class Meta:
		model = Users
		fields = 'userid','givenname','role','bu','lastlogin'
		# widgets = {
        #     'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        # }

class ProjectADD(ModelForm):
	class Meta:
		model=Projects
		fields= 'project_num', 'project' , 'active', 'project_type', 'bu_num', 'project_description'

class ProgramADD(ModelForm):
	class Meta:
		model=Programs
		fields= 'program_num', 'program'
		#, 'active', 'project_type', 'bu_id', 'project_description'

class ContractorTrackerADD(ModelForm):
	class Meta:
		model=ContractorTracker
		fields= '__all__'
		#, 'active', 'project_type', 'bu_id', 'project_description'

# class PurchaseOrdersADD(ModelForm):
# 	class Meta:
# 		model=PurchaseOrders
# 		fields= '__all__'
# 		#, 'active', 'project_type', 'bu_id', 'project_description'