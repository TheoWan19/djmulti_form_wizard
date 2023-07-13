from django.shortcuts import render
from . forms import ApplicantDetailsForm, AcademicQualitificationForm, AcademicQualificationFormSet
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage 

# Create your views here.
def home(request):
	return render(request, 'accounts/home.html')

class ApplicantWizardView(SessionWizardView):
	file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'files'))
	form_list = [ApplicantDetailsForm, AcademicQualificationFormSet]
	template_name = 'accounts/form.html'	
	initial_dict = initial
