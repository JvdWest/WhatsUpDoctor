from django.db import models
from django.conf import settings


class AuditableFields(models.Model):
    create_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        related_name="%(class)s_created_by")
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        related_name="%(class)s_last_modified_by")
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


# To be applied to all linking tables
class EffectiveRangeDates(models.Model):
    effective_start_date = models.DateTimeField()
    effective_end_date = models.DateTimeField()

    class Meta:
        abstract = True


class Patient(AuditableFields):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=13)


class Practitioner(AuditableFields):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=13)
    hpcsa_number = models.CharField(max_length=10)
    # Can be done with this, but requires auditable fields
    # patients = models.ManyToManyField(Patient)


class PractitionerPatient(AuditableFields, EffectiveRangeDates):
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT)  # Prevents accidental deletion
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
