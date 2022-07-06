from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
	accounts = (
			('select account', 'select account'),
			('HOD', 'HOD'),
			('lecturer', 'lecturer'),
			('Assessment committee', 'Assessment committee'),
		)
	account_type = models.CharField(max_length=200, choices=accounts, default='select account')
	email = models.CharField(max_length = 200, blank=True, unique=True)
	first_name = models.CharField(max_length=200, blank=True)
	last_name = models.CharField(max_length=200, blank=True)
	username = models.CharField(max_length = 200, blank=True, unique=True)
	date_created = models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	def __str__(self):
		return self.username


class StaffAppraisal(models.Model):
	marital_status = (
			('select account', 'select account'),
			('single', 'single'),
			('married', 'married'),
			('divorced', 'divorced'),
		)
	appointment_status = (
			('select account', 'select account'),
			('Yes','Yes'),
			('No','No'),
		)
	marital_status = models.CharField(max_length=100, choices=marital_status, default='select account')
	college = models.CharField(max_length=200, blank=True)
	department = models.CharField(max_length=200, blank=True)
	date_of_first_appointment = models.DateField(blank=True)
	grade_of_first_appointment = models.CharField(blank=True, max_length=200)
	date_of_last_promotion = models.DateField(blank=True)
	grade_of_last_promotion = models.CharField(blank=True, max_length=200)
	date_of_current_appointment = models.DateField(blank=True)
	grade_of_current_appointment = models.CharField(blank=True, max_length=200)
	appointment_confirmation = models.CharField(max_length=100, choices=appointment_status, default='select account')
	present_salary = models.CharField(blank=True, max_length=200)
	academic_qualification_degree = models.CharField(max_length=200, blank=True)
	academic_qualification_class = models.CharField(max_length=200, blank=True)
	academic_qualification_institution = models.CharField(max_length=200, blank=True)
	date_of_award = models.DateField()
	professional_qualification = models.CharField(blank=True, max_length=200)
	professional_awarding_body = models.CharField(max_length=200, blank=True)
	professional_date_of_award = models.DateField()
	teaching_experience_institution = models.CharField(max_length=200, blank=True)
	designation = models.CharField(max_length=200, blank=True)
	specialization = models.CharField(blank=True, max_length=200)
	period_from = models.DateField()
	period_to = models.DateField()
	courses_taught_during_harmattan = models.CharField(blank=True, max_length=600)
	courses_taught_during_rain = models.CharField(blank=True, max_length=600)
	professional_employer = models.CharField(blank=True, max_length=200)
	designation = models.CharField(max_length=200, blank=True)
	nature_of_duty = models.CharField(blank=True, max_length=200)
	professional_experience_date = models.DateField()
	publications = models.FileField(upload_to='files/')
	research_topic = models.CharField(max_length=500, blank=True)
	research_date = models.CharField(max_length=200, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='lecturer',)
	date_submitted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.research_topic} by {str(self.user)}'

	def get_absolute_url(self):
		return reverse('appraisal:appraisal-detail', kwargs={'pk': self.pk})


class HODAssessment(models.Model):
	grades = (
			('A','A'),
			('B','B'),
			('C','C'),
			('D','D'),
			('E','E'),
		)
	recommendation_option = (
			('select', 'select'),
			('Approved','Approved'),
			('Unapproved', 'Unapproved'),
		)
	signature_option = (
			('select', 'select'),
			('Signed & Approved','Signed & Approved'),
			('Unsigned &Unapproved', 'Unsigned &Unapproved'),
		)
	quality_of_teaching = models.CharField(max_length=200, choices=grades)
	current_research = models.CharField(max_length=200, choices=grades)
	quality_of_research = models.CharField(max_length=200, choices=grades)
	quality_of_publications = models.CharField(max_length=200, choices=grades)
	postgraduate_supervision = models.CharField(max_length=200, choices=grades)
	other_departmental_responsibilities = models.CharField(max_length=200, choices=grades)
	contribution_to_university_or_country = models.CharField(max_length=200, choices=grades)
	general_assessment = models.CharField(max_length=200, choices=grades)
	recommendations = models.CharField(blank=True, default='select', max_length=200, choices=recommendation_option)
	signature = models.CharField(blank=True, max_length=200, default='select', choices=signature_option)
	date_signed = models.DateTimeField(auto_now_add=True)
	lecturer = models.ForeignKey(StaffAppraisal, on_delete=models.CASCADE, null=True, blank=True, related_name='lecturer_form')
	hod_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='hod_fullname')

	def __str__(self):
		return f'Remarks by {self.hod_name} on {self.lecturer.research_topic} by {self.lecturer.user}'
	
	def get_absolute_url(self):
		return reverse('appraisal:approved-appraisals')

class LecturerComment(models.Model):
	signature_option = (
		('select', 'select'),
		('Signed & Approved','Signed & Approved'),
		('Unsigned &Unapproved', 'Unsigned &Unapproved'),
	)
	get_comment = models.TextField()
	get_lecturer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default='No comment', related_name='lecturer_name')
	get_appraisal = models.ForeignKey(HODAssessment, on_delete=models.CASCADE, null=True, blank=True, related_name='lecturer_comment')
	date_signed = models.DateTimeField(auto_now_add=True)
	get_signature = models.CharField(blank=True, max_length=200, default='select', choices=signature_option)

	def __str__(self):
		return f"Appraisal {self.get_appraisal.lecturer.research_topic} and ID {self.get_appraisal.id} with lecturer comment \
		'{self.get_comment}'"

	def get_absolute_url(self):
		return reverse('appraisal:appraisal-detail', kwargs={'pk': self.pk})

class CPCAssessment(models.Model):
	grades = (
			('Select', 'Select'),
			('A','A'),
			('B','B'),
			('C','C'),
			('D','D'),
			('E','E'),
		)
	score = (
			('Select', 'Select'),
			('5','5'),
			('10','10'),
			('15','15'),
		)
	signature_option = (
			('select', 'select'),
			('Signed & Approved','Signed & Approved'),
			('Unsigned &Unapproved', 'Unsigned &Unapproved'),
		)
	quality_of_teaching_grade = models.CharField(blank=True, max_length=200, default='Select', choices=grades)
	quality_of_research_grade = models.CharField(blank=True, max_length=200, default='Select', choices=grades)
	quality_of_publication_grade = models.CharField(blank=True, max_length=200, default='Select', choices=grades)
	contribution_to_university_or_country_grade = models.CharField(max_length=200, blank=True, default='Select', choices=grades)
	academic_qualification_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)] , default=0)
	professional_qualification_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
	teaching_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)], default=0)
	current_research_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
	recognized_publication_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)], default=0)
	contribution_to_university_or_country_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
	administrative_experience_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
	interview_performance_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
	which_appraisal = models.ForeignKey(LecturerComment, on_delete=models.CASCADE, null=True, blank=True, related_name='which_lecturer')
	cpc_member = models.ForeignKey(User, on_delete=models.CASCADE,null=True,  blank=True, default='cpc_staff', related_name='member_of_staff')
	percentage = models.CharField(max_length=100, blank=True, default=0.0)
	remarks = models.CharField(max_length=200, blank=True, default='no remarks yet!')
	board_recommendations = models.CharField(max_length=500, blank=True)
	dean_signature = models.CharField(blank=True, max_length=200, default='select', choices=signature_option)
	date_signed = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return  f'Board percentage for {str(self.which_appraisal)} is {self.percentage}'

	def get_absolute_url(self):
		return reverse('appraisal:approved-appraisals')


