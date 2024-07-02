from django.contrib import admin
from .models import Developer,Recruiter,Company,Competence,JobOffer

# Register your models here.
admin.site.register(Developer)
admin.site.register(Recruiter)
admin.site.register(Company)
admin.site.register(Competence)
admin.site.register(JobOffer)