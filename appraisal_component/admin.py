from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(StaffAppraisal)

@admin.register(HODAssessment)
class HODAssessmentAdmin(admin.ModelAdmin):
	list_display = ('hod_name', 'lecturer', 'quality_of_research','quality_of_teaching', 'current_research', 'quality_of_publications', \
			 'postgraduate_supervision','other_departmental_responsibilities', 'contribution_to_university_or_country', \
					'general_assessment',  'recommendations', 'signature', 'date_signed')
admin.site.register(LecturerComment)
admin.site.register(CPCAssessment)
