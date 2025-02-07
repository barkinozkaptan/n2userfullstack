
import json
from django.core.management.base import BaseCommand
from core_user.models import User, Address, Geo, Company

# NOTE: Adjust the path if your JSON is elsewhere.
USERS_JSON_FILE = 'data/users.json'

class Command(BaseCommand):
    help = "Import users from a JSON file."

    def handle(self, *args, **options):
        with open(USERS_JSON_FILE, 'r') as f:
            users_data = json.load(f)

        for user_dict in users_data:
            # Extract nested data
            address_data = user_dict.pop('address')
            geo_data = address_data.pop('geo')
            company_data = user_dict.pop('company')

            # Create the related objects
            geo = Geo.objects.create(**geo_data)
            address = Address.objects.create(geo=geo, **address_data)
            company = Company.objects.create(
                name=company_data['name']
            )
            # If your model has 'catchPhrase' and 'bs', 
            # you need to add those fields to `Company` model or ignore them.

            # Create the main User record
            # You can ignore 'id' if you want Django to auto-increment
            user_id = user_dict.pop('id', None)
            user = User.objects.create(
                id=user_id,  # or remove if you want auto PK
                address=address,
                company=company,
                **user_dict
            )

            self.stdout.write(self.style.SUCCESS(
                f"Imported user: {user.username}"
            ))
