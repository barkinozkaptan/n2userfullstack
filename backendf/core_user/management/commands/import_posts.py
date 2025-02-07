import json
from django.core.management.base import BaseCommand
from core_post.models import Post
from core_user.models import User  # Import User model

# Path to the posts JSON file
POSTS_JSON_FILE = "data/posts.json"

class Command(BaseCommand):
    help = "Import posts from a JSON file."

    def handle(self, *args, **options):
        try:
            with open(POSTS_JSON_FILE, "r") as f:
                posts_data = json.load(f)
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"❌ File not found: {POSTS_JSON_FILE}"))
            return
        
        posts_created = 0

        for post_dict in posts_data:
            user_id = post_dict.pop("userId", None)

            if user_id is None:
                self.stderr.write(self.style.WARNING(f"⚠️ Skipping post with missing userId: {post_dict}"))
                continue
            
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                self.stderr.write(self.style.WARNING(f"⚠️ Skipping post {post_dict['title']} (User ID {user_id} not found)"))
                continue

            # Create post
            post, created = Post.objects.get_or_create(
                user=user,
                title=post_dict["title"],
                body=post_dict["body"],
            )
            if created:
                posts_created += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Imported {posts_created} posts successfully!"))
