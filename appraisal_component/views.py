from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import User, StaffAppraisal as Staff, HODAssessment as HOD, CPCAssessment as CPC, LecturerComment
from appraisal_component.models import User
from django.views.generic import ( ListView, DetailView, CreateView, UpdateView, DeleteView )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.urls import reverse
from .forms import *

# Appraisal Views
class AppraisalCreateView(LoginRequiredMixin, CreateView):
	model = Staff
	fields = '__all__'

	#exclude = ['user']
	#redirect = 'staff-list'
	#success_url = reverse('appraisal:appraisal-list')

	#overriding the form valid method
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class AppraisalListView(ListView):
	model = Staff
	context_object_name = 'all_applications'
	ordering = ['-date_submitted'] 
	paginate_by = 7


class AppraisalDetailView(DetailView):
	model = Staff


class AppraisalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Staff
	fields = '__all__'
	exclude = ['user', 'date_submitted']
	
	def form_valid(self, form):
		form.instance.user  = self.request.user
		return super().form_valid(form)

	def test_func(self):
		authorized_staff = self.get_object()
		if self.request.user == authorized_staff.user:
			return True
		return False

class AppraisalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Staff
	success_url = '/'

	def test_func(self):
		authorized_staff = self.get_object()
		if self.request.user == authorized_staff.user:
			return True
		return False

# Staff Views
class StaffListView(ListView):
	model = User
	template_name = 'appraisal_component/all_staff.html' 
	context_object_name = 'total_staff'
	ordering = ['-date_joined'] 
	paginate_by = 7

	def get_queryset(self):
		lecturers = User.objects.filter(account_type='lecturer')
		return lecturers


class StaffAppraisalListView(ListView):
	model = Staff
	template_name = 'appraisal_component/staff_appraisals.html'
	context_object_name = 'user_appraisals'
	ordering = ['-date_submitted']
	paginate_by = 5

	def get_queryset(self):
		#getting the username from the url 
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		print('current staff: ', user)
		staff = Staff.objects.filter(user=user).order_by('-date_submitted')
		#hod = HOD.objects.filter(hod_name=user).order_by('-date_signed')
		return staff

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		staff = Staff.objects.filter(user=user).order_by('-date_submitted')

		staff_count = staff.count()
		hod = HOD.objects.filter(hod_name=user).order_by('-date_signed')
		approved_appraisal_count = hod.count()
		cpc_member = CPC.objects.filter(cpc_member=user).order_by('-date_signed')
		cpc_member_count = cpc_member.count()
		context = {
		'hod': hod,
		'staff':staff,
		'staff_count':staff_count,
		'approved_appraisal_count':approved_appraisal_count,
		'cpc_member':cpc_member,
		'cpc_member_count':cpc_member_count,
		}
		return context


# HOD Views
class RemarksCreateView(LoginRequiredMixin, CreateView):
	model = HOD
	context_object_name = 'hod_assessment'
	#fields = ('quality_of_teaching', 'current_research', 'quality_of_publications', 'hod_name', 'recommendations', )
	fields = '__all__'

	#overriding the form valid method
	def form_valid(self, form):
		form.instance.hod_name  = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		hod = HOD.objects.all()
		context['hod_assessment'] = hod
		print('this is the context: ',context)
		return context


	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		hod_name = HOD.objects.filter(hod_name=user)
		print('hod name is:', hod_name)
		hod_assessment = HOD.objects.all()
		for i in hod_assessment:
			lecturer = i.lecturer.user.username
			print('this is the lecturer: ',lecturer)
		return lecturer


class ApprovedAppraisalListView(ListView):
	model = HOD
	context_object_name = 'approved_appraisals'
	ordering = ['-date_signed'] #0650503440, gtb, 4040-ussd pin
	paginate_by = 7

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		current_user = self.request.user
		print('this is the current_user and the account_type: ', current_user, current_user.account_type)
		approved_appraisals = HOD.objects.all()
		approved_appraisals_with_lecturer_comments = LecturerComment.objects.all()
		context = {
			'current_user':current_user,
			'approved_appraisals':approved_appraisals,
			'approved_appraisals_with_lecturer_comments':approved_appraisals_with_lecturer_comments,
		}
		return context


class LecturerCommentCreateView(LoginRequiredMixin, CreateView):
	model = LecturerComment
	context_object_name = 'lecturer_comment'
	fields = '__all__'
	#exclude = ['get_appraisal']

	def form_valid(self, form):
		form.instance.get_lecturer = self.request.user
		form = super().form_valid(form)
		print('form details: ', form)
		return form


class CPCCreateView(LoginRequiredMixin, CreateView):
	model = CPC
	context_object_name = 'cpc_assessment'
	fields = '__all__'
	exclude = ['remarks', 'percentage']

	#overriding the form valid method
	def form_valid(self, form):
		form.instance.cpc_member  = self.request.user
		academic_qualification_score = form.instance.academic_qualification_score
		professional_qualification_score = form.instance.professional_qualification_score
		teaching_score = form.instance.teaching_score
		current_research_score = form.instance.current_research_score
		recognized_publication_score = form.instance.recognized_publication_score
		contribution_to_university_or_country_score = form.instance.contribution_to_university_or_country_score
		administrative_experience_score = form.instance.administrative_experience_score
		interview_performance_score = form.instance.interview_performance_score
		percentage = form.instance.percentage
		print('current appraisal percentage = ', percentage)

		board_scores = [academic_qualification_score, professional_qualification_score, teaching_score,
		current_research_score, recognized_publication_score, contribution_to_university_or_country_score, 
		administrative_experience_score, interview_performance_score]

		new_percentage = sum(board_scores) / len(board_scores)
		new_percentage = new_percentage * 10
		main_percentage = form.instance.percentage = new_percentage
		print('main percentage = ', main_percentage)

		# provide percentage remark based on the percentage grade
		if main_percentage >= 70:
			form.instance.remarks = 'Distinction!'
		elif main_percentage >= 50 and main_percentage < 70:
			form.instance.remarks = 'Fair!'
		else:
			form.instance.remarks = 'Okay'
		return super().form_valid(form)

	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cpc = get_object_or_404(LecturerComment, get_appraisal=self.kwargs.get('pk'))
		context['cpc'] = cpc
		return context

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		cpc_member = CPC.objects.filter(cpc_member=user)
		print('member of committee name is:', cpc_member)
		return cpc_member



class CPCListView(ListView):
	model = CPC
	context_object_name = 'board_approved_appraisals'
	ordering = ['date_signed'] #0650503440, gtb, 4040-ussd pin
	paginate_by = 2

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		current_user = self.request.user
		board_approved_appraisals = CPC.objects.all()
		context = {'board_approved_appraisals':board_approved_appraisals, 'current_user':current_user}
		return context

	

	