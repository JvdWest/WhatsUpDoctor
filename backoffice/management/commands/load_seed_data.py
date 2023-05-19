import random
from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from backoffice.models import Patient, Practitioner, PractitionerPatient
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Load seed data'

    def handle(self, *args, **options):
        # Create and save seed data

        user = User(
            username='admin',
            email='admin@example.com',
            password='admin'
        )
        user.save()

        patients = []
        seed_data = [
            {
                'first_name': 'John',
                'last_name': 'Doe',
                'id_number': '1234567890123'
            },
            {
                'first_name': 'Jane',
                'last_name': 'Smith',
                'id_number': '0987654321'
            },
            {
                'first_name': 'Michael',
                'last_name': 'Johnson',
                'id_number': '9876543210123'
            },
            {
                'first_name': 'Alice',
                'last_name': 'Anderson',
                'id_number': '5555555555123'
            },
            {
                'first_name': 'Robert',
                'last_name': 'Williams',
                'id_number': '2222222222123'
            },
            {
                'first_name': 'Emily',
                'last_name': 'Brown',
                'id_number': '3333333333123'
            },
            {
                'first_name': 'Daniel',
                'last_name': 'Davis',
                'id_number': '4444444444123'
            },
            {
                'first_name': 'Olivia',
                'last_name': 'Martinez',
                'id_number': '6666666666123'
            },
            {
                'first_name': 'Sophia',
                'last_name': 'Taylor',
                'id_number': '7777777777123'
            },
            {
                'first_name': 'Ethan',
                'last_name': 'Thomas',
                'id_number': '8888888888123'
            }
        ]

        for data in seed_data:
            patient = Patient(
                first_name=data['first_name'],
                last_name=data['last_name'],
                id_number=data['id_number'],
                create_by=user,
                last_modified_by=user
            )
            patient.save()
            patients.append(patient)

        seed_data = [
            {
                'first_name': 'Alice',
                'last_name': 'Anderson',
                'id_number': '5555555555',
                'hpcsa_number': 'A1234567'
            },
            {
                'first_name': 'Bob',
                'last_name': 'Brown',
                'id_number': '6666666666',
                'hpcsa_number': 'B9876543'
            },
            {
                'first_name': 'Carol',
                'last_name': 'Clark',
                'id_number': '7777777777',
                'hpcsa_number': 'C2468135'
            },
            {
                'first_name': 'David',
                'last_name': 'Davis',
                'id_number': '8888888888',
                'hpcsa_number': 'D1357924'
            },
            {
                'first_name': 'Eve',
                'last_name': 'Evans',
                'id_number': '9999999999',
                'hpcsa_number': 'E7531902'
            }
        ]

        practitioners = []
        for data in seed_data:
            practitioner = Practitioner(
                first_name=data['first_name'],
                last_name=data['last_name'],
                id_number=data['id_number'],
                hpcsa_number=data['hpcsa_number'],
                create_by=user,
                last_modified_by=user
            )
            practitioner.save()
            practitioners.append(practitioner)

        # Random assignments
        for practitioner in practitioners:
            random_number = random.choice([1, 2])
            if random_number == 2:
                continue
            for patient in patients:
                random_number = random.choice([1, 2])
                if random_number == 1:
                    continue
                practitioner_patient = PractitionerPatient(
                    practitioner=practitioner,
                    patient=patient,
                    effective_start_date=make_aware(datetime(2023, 1, 1)),
                    effective_end_date=make_aware(datetime(2023, 12, 31)),
                    create_by=user,
                    last_modified_by=user
                )
                practitioner_patient.save()

        self.stdout.write(self.style.SUCCESS('Seed data loaded successfully.'))
