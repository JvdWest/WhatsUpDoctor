from django.contrib import admin

from backoffice.models import Patient, Practitioner

# Register your models here.
admin.site.register(Patient)
admin.site.register(Practitioner)