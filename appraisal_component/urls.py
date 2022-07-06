from django.urls import path
from . import views 
from .views import (
 StaffListView,
 StaffAppraisalListView, 
 AppraisalDetailView,
 AppraisalCreateView,
 AppraisalUpdateView,
 AppraisalDeleteView,
 AppraisalListView,
 RemarksCreateView,
 ApprovedAppraisalListView,
 LecturerCommentCreateView,
 CPCCreateView,
 CPCListView,
 )

app_name = 'appraisal'

urlpatterns = [
    path('appraisal/apply/', AppraisalCreateView.as_view(), name='apply'),
    path('all-appraisals/', AppraisalListView.as_view(), name='appraisal-list'),
    path('staff/appraisal/<int:pk>/', AppraisalDetailView.as_view(), name='appraisal-detail'),
    path('staff/appraisal/<int:pk>/update', AppraisalUpdateView.as_view(), name='appraisal-update'),
    path('staff/appraisal/<int:pk>/delete', AppraisalDeleteView.as_view(), name='appraisal-delete'),

    path('staff/', StaffListView.as_view(), name='staff-list'),
    path('staff/<str:username>', StaffAppraisalListView.as_view(), name='staff-detail'),

    path('hod/remarks/', RemarksCreateView.as_view(), name='add-remarks'),
    path('approved-appraisals/', ApprovedAppraisalListView.as_view(), name='approved-appraisals'),

    path('lecturer-comment/appraisal/<int:pk>/', LecturerCommentCreateView.as_view(), name='lecturer-comment'),

    path('board-assessment/comment/<int:pk>/', CPCCreateView.as_view(), name='board-comment'),
    path('board-approved-appraisals/', CPCListView.as_view(), name='board-approved-appraisals'),
]