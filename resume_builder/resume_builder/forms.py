from django import forms
from django.forms import modelformset_factory
from .models import Personal_info, Education, Skill, WorkExperience, Project, Certificate

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = Personal_info
        fields = ['full_name', 'email', 'phone', 'location', 'career_summary']
        widgets = {
            'career_summary': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

EducationFormSet = modelformset_factory(
    Education,
    fields=['degree', 'institution', 'graduation_year'],
    extra=1,
    can_delete=True,
    widgets={
        'degree': forms.TextInput(attrs={'class': 'form-control'}),
        'institution': forms.TextInput(attrs={'class': 'form-control'}),
        'graduation_year': forms.NumberInput(attrs={'class': 'form-control'}),
    }
)

SkillFormSet = modelformset_factory(
    Skill,
    fields=['name'],
    extra=3,
    can_delete=True,
    widgets={
        'name': forms.TextInput(attrs={'class': 'form-control'}),
    }
)

WorkExperienceFormSet = modelformset_factory(
    WorkExperience,
    fields=['position', 'company', 'start_date', 'end_date', 'description'],
    extra=1,
    can_delete=True,
    widgets={
        'position': forms.TextInput(attrs={'class': 'form-control'}),
        'company': forms.TextInput(attrs={'class': 'form-control'}),
        'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
    }
)

ProjectFormSet = modelformset_factory(
    Project,
    fields=['title', 'description'],
    extra=1,
    can_delete=True,
    widgets={
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
    }
)

CertificateFormSet = modelformset_factory(
    Certificate,
    fields=['title', 'issuer', 'date_obtained', 'description'],
    extra=1,
    can_delete=True,
    widgets={
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'issuer': forms.TextInput(attrs={'class': 'form-control'}),
        'date_obtained': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        'description': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
    }
)