from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('template-selection/', views.template_selection, name='template_selection'),
    path('resume-wizard/<int:template>/', views.resume_wizard, name='resume_wizard'),
    path('resume-wizard/<int:template>/<int:step>/', views.resume_wizard, name='resume_wizard_step'),
    path('resume-preview/', views.resume_preview, name='resume_preview'),
    path('enhance-text/', views.enhance_text, name='enhance_text'),
]