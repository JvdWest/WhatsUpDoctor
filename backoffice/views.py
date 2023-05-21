import datetime
import json
from backoffice.models import Patient
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime


def get_patients(request):
    hpcsa_number = request.GET.get('hpcsanumber')

    current_date = datetime.utcnow().astimezone()
    if hpcsa_number is None:
        queryset = Patient.objects.filter(is_deleted=False)
    else:
        queryset = Patient.objects.filter(
            practitionerpatient__practitioner__hpcsa_number__exact=hpcsa_number,
            practitionerpatient__effective_start_date__lt=current_date,
            practitionerpatient__effective_end_date__gt=current_date,
            is_deleted=False,
            practitionerpatient__is_deleted=False,
            practitionerpatient__practitioner__is_deleted=False)

    serialized_data = serializers.serialize('json', queryset)
    json_data = json.loads(serialized_data)

    # Return the serialized data as a JSON response
    return JsonResponse(json_data, safe=False)
