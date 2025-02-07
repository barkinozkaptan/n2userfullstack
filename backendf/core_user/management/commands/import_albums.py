import json
from django.core.management.base import BaseCommand
from core_album.models import Album
from core_user.models import User  # Import User model

# Path to the albums JSON file
ALBUMS_JSON_FILE = "data/albums.json"

class Command(BaseCommand):
    help = "Import albums from a JSON file."

    def handle(self, *args, **options):
        try:
            with open(ALBUMS_JSON_FILE, "r") as f:
                albums_data = json.load(f)
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"❌ File not found: {ALBUMS_JSON_FILE}"))
            return
        
        albums_created = 0

        for album_dict in albums_data:
            user_id = album_dict.pop("userId", None)

            if user_id is None:
                self.stderr.write(self.style.WARNING(f"⚠️ Skipping album with missing userId: {album_dict}"))
                continue
            
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                self.stderr.write(self.style.WARNING(f"⚠️ Skipping album '{album_dict['title']}' (User ID {user_id} not found)"))
                continue

            # Create album
            album, created = Album.objects.get_or_create(
                user=user,
                title=album_dict["title"],
            )
            if created:
                albums_created += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Imported {albums_created} albums successfully!"))
