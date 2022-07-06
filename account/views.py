from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
#from appraisal_app.models import StaffAppraisals as StaffAppraisal
from appraisal_component.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm


# Create your views here.
@login_required
def dashboard(request):
	user = request.user
	context = {
		'user':user, 
		}
	return render(request, 'account/dashboard.html', context)

def register (request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			# Create a new user object but avoid saving it yet
			new_user = user_form.save(commit=False)
			# Set the chosen password:using the set_password() allows encryption
			new_user.set_password(user_form.cleaned_data['password'])
			# Save the User object
			new_user.save()
			# Create the user profile
			Profile.objects.create(user=new_user)
			return redirect ('login')
			#return render (request, 'account/login.html', {'new_user':new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'account/register.html', {'user_form':user_form})

@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile,
										data = request.POST,
										files = request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, f'Profile updated successfully!')
		else: 
			messages.warning(request, f'Error updating your profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)

	return render(request, 'account/edit.html',
							{'user_form':user_form,
							'profile_form':profile_form})