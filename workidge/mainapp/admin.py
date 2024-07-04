from django.contrib import admin
from .models import Developer,Recruiter,Company,Competence,JobOffer

# Register your models here.
#admin.site.register(Developer)
admin.site.register(Recruiter)
admin.site.register(Company)
#admin.site.register(Competence)
admin.site.register(JobOffer)

from .models import Competence

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'created', 'modified')
    search_fields = ('name',)
    filter_horizontal = ('subskills',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.save()
        else:
            super().save_model(request, obj, form, change)


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('id','email','name','surname','pn','title')
    search_fields = ('name',)
    filter_horizontal = ('skills',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.save()
        else:
            super().save_model(request, obj, form, change)