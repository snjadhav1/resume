from django.db import models

class Personal_info(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    career_summary = models.TextField()

class Education(models.Model):
    Personal_info = models.ForeignKey(Personal_info, related_name='education', on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    graduation_year = models.IntegerField()

class Skill(models.Model):
    Personal_info = models.ForeignKey(Personal_info, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class WorkExperience(models.Model):
    Personal_info = models.ForeignKey(Personal_info, related_name='work_experiences', on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

class Project(models.Model):
    Personal_info = models.ForeignKey(Personal_info, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Certificate(models.Model):
    Personal_info = models.ForeignKey(Personal_info, related_name='certificates', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    date_obtained = models.DateField()
    description = models.TextField(blank=True)

class Personal_infoTemplate(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    preview_image = models.ImageField(upload_to='Personal_info_templates/')
    html_template = models.TextField()
    css_template = models.TextField()
