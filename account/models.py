from appraisal_component.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
	gender = (
			('select', 'select'),
			('male', 'male'),
			('female', 'female')
		)
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	dob = models.DateField(blank=True, null=True)
	bio = models.CharField(max_length=200, blank=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d', default='media/default.jpeg', blank=True)
	level = models.CharField(max_length=200, blank=True, default='junior')
	gender = models.CharField(max_length=100, choices=gender, default='select')
	department = models.CharField(max_length=200, blank=True)
	nationality = models.CharField(max_length=100, blank=True, default='Nigeria')
	state = models.CharField(max_length=100, blank=True, default='Ogun')
	phone_no = models.CharField(max_length=100, blank=True)
	staff_id = models.CharField(max_length=100, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	last_seen = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)