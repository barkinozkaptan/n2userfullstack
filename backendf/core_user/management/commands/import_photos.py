import json
from django.core.management.base import BaseCommand
from core_photo.models import Photo
from core_album.models import Album  # Import the Album model

# Path to the photos JSON file
PHOTOS_JSON_FILE = "data/photos.json"

class Command(BaseCommand):
    help = "Import photos from a JSON file."

    def handle(self, *args, **options):
        try:
            with open(PHOTOS_JSON_FILE, "r") as f:
                photos_data = json.load(f)
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"❌ File not found: {PHOTOS_JSON_FILE}"))
            return
        
        photos_created = 0

        for photo_dict in photos_data:
            album_id = photo_dict.pop("albumId", None)

            if album_id is None:
                self.stderr.write(self.style.WARNING(f"⚠️ Skipping photo with missing albumId: {photo_dict}"))
                continue
            
            try:
                album = Album.objects.get(id=album_id)
            except Album.DoesNotExist:
                self.stderr.write(self.style.WARNING(f"⚠️ Skipping photo '{photo_dict['title']}' (Album ID {album_id} not found)"))
                continue

            # Create photo
            photo, created = Photo.objects.get_or_create(
                album=album,
                title=photo_dict["title"],
                url=photo_dict["url"],
                thumbnail_url=photo_dict["thumbnailUrl"]
            )
            if created:
                photos_created += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Imported {photos_created} photos successfully!"))
