import json

from backoffice.models import Patient
from django.http import JsonResponse
from django.core import serializers


def get_patients(request):
    hpcsa_number = request.GET.get('hpcsanumber')

    if hpcsa_number is None:
        return JsonResponse({'error': 'The hpcsanumber parameter is missing.'}, status=400)

    queryset = Patient.objects.filter(practitionerpatient__practitioner__hpcsa_number__exact=hpcsa_number)

    serialized_data = serializers.serialize('json', queryset)
    json_data = json.loads(serialized_data)

    # Return the serialized data as a JSON response
    return JsonResponse(json_data, safe=False)
