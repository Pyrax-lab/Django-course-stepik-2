from django.core.management.base import BaseCommand
from faker import Faker
from hr.models import Employee


class Command(BaseCommand):

    help = "Generate fake users"

    def handle(self, *args, **kwargs):
        fake = Faker()
        count = 30000

        for i in range(count):
            employee = Employee(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                about = fake.text(max_nb_chars=10000),
                age=fake.random_int(min=16, max=89)
            )
            
            employee.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} fake users!'))