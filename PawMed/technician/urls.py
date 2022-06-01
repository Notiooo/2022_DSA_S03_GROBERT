from django.urls import path

from .views import SubmitResultView, HeadTechnicianApprovalView, TechnicianHomepageView

urlpatterns = [
    path('submit/', SubmitResultView.as_view(), name="technician_submit_result"),
    path('approval/', HeadTechnicianApprovalView.as_view(), name="head_technician_approval_view"),
    path('home/', TechnicianHomepageView.as_view(), name='technician_home')
]