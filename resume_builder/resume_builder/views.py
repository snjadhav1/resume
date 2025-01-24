from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Personal_info, Education, Skill, WorkExperience, Project, Certificate, Personal_infoTemplate
from .forms import (PersonalInfoForm, EducationFormSet, SkillFormSet, 
                    WorkExperienceFormSet, ProjectFormSet, CertificateFormSet)
import google.generativeai as genai

def home(request):
    return render(request, 'resume_builder/home.html')

def template_selection(request):
    return render(request, 'resume_builder/template_selection.html')

def resume_wizard(request, template, step=1):
    resume_id = request.session.get('resume_id')
    
    if resume_id:
        resume = Personal_info.objects.get(id=resume_id)
    else:
        resume = None

    if request.method == 'POST':
        if step == 1:
            form = PersonalInfoForm(request.POST, instance=resume)
            if form.is_valid():
                resume = form.save(commit=False)
                resume.template = template
                resume.save()
                request.session['resume_id'] = resume.id
                return redirect('resume_wizard_step', template=template, step=step+1)
        elif step == 2:
            formset = EducationFormSet(request.POST, queryset=Education.objects.filter(Personal_info=resume))
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.Personal_info = resume
                    instance.save()
                return redirect('resume_wizard_step', template=template, step=step+1)
        elif step == 3:
            formset = SkillFormSet(request.POST, queryset=Skill.objects.filter(Personal_info=resume))
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.Personal_info = resume
                    instance.save()
                return redirect('resume_wizard_step', template=template, step=step+1)
        elif step == 4:
            formset = WorkExperienceFormSet(request.POST, queryset=WorkExperience.objects.filter(Personal_info=resume))
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.Personal_info = resume
                    instance.save()
                return redirect('resume_wizard_step', template=template, step=step+1)
        elif step == 5:
            project_formset = ProjectFormSet(request.POST, queryset=Project.objects.filter(Personal_info=resume))
            certificate_formset = CertificateFormSet(request.POST, queryset=Certificate.objects.filter(Personal_info=resume))
            if project_formset.is_valid() and certificate_formset.is_valid():
                for formset in [project_formset, certificate_formset]:
                    instances = formset.save(commit=False)
                    for instance in instances:
                        instance.Personal_info = resume
                        instance.save()
                return redirect('resume_preview')
    else:
        if step == 1:
            form = PersonalInfoForm(instance=resume)
        elif step == 2:
            formset = EducationFormSet(queryset=Education.objects.filter(Personal_info=resume))
        elif step == 3:
            formset = SkillFormSet(queryset=Skill.objects.filter(Personal_info=resume))
        elif step == 4:
            formset = WorkExperienceFormSet(queryset=WorkExperience.objects.filter(Personal_info=resume))
        elif step == 5:
            project_formset = ProjectFormSet(queryset=Project.objects.filter(Personal_info=resume))
            certificate_formset = CertificateFormSet(queryset=Certificate.objects.filter(Personal_info=resume))

    context = {
        'step': step,
        'resume': resume,
        'template': template,
    }

    if step == 1:
        context['form'] = form
    elif step == 5:
        context['project_formset'] = project_formset
        context['certificate_formset'] = certificate_formset
    else:
        context['formset'] = formset

    if template == 1:
        return render(request, 'resume_builder/wizard1.html', context)
    elif template == 2:
        return render(request, 'resume_builder/wizard2.html', context)
    elif template == 3:
        return render(request, 'resume_builder/wizard3.html', context)
    elif template == 4:
        return render(request, 'resume_builder/wizard4.html', context)
    elif template == 5:
        return render(request, 'resume_builder/wizard5.html', context)
    elif template == 6:
        return render(request, 'resume_builder/wizard6.html', context)
    else:
        return redirect('template_selection')

def resume_preview(request):
    resume_id = request.session.get('resume_id')
    if not resume_id:
        return redirect('home')
    
    resume = Personal_info.objects.get(id=resume_id)
    
    context = {
        'resume': resume,
    }
    return render(request, 'resume_builder/preview.html', context)

@csrf_exempt
@require_POST
def enhance_text(request):
    text = request.POST.get('text', '')
    genai.configure(api_key='AIzaSyDpLRxNFHhgt0VqZTv1YLtS-NU02fkXGQc')
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(f"Enhance the following text for a resume in the paragraph of 3  lines and don't give any heading,star symbols, highlights in the text: {text}")
    return JsonResponse({'enhanced_text': response.text})