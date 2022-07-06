from django import forms
from .models import StaffAppraisal, HODAssessment, CPCAssessment, LecturerComment

class StaffAppraisalForm(forms.ModelForm):
	class Meta:
		model = StaffAppraisal
		fields = '__all__'
		#fields = ('course_title','course_code','invigilator','room', 'description', 'completed', 'exam_date')

class HODAssessmentForm(forms.ModelForm):
	class Meta:
		model = HODAssessment
		fields = '__all__'


class LecturerCommentForm(forms.ModelForm):
	class Meta:
		model = LecturerComment
		fields = '__all__'


class CPCAssessmentForm(forms.ModelForm):
	class Meta:
		model = CPCAssessment
		fields = '__all__'
