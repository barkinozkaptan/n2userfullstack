import json
from django.core.management.base import BaseCommand
from core_comment.models import Comment
from core_post.models import Post  # Import Post model

# Path to the comments JSON file
COMMENTS_JSON_FILE = "data/comments.json"

class Command(BaseCommand):
    help = "Import comments from a JSON file."

    def handle(self, *args, **options):
        try:
            with open(COMMENTS_JSON_FILE, "r") as f:
                comments_data = json.load(f)
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"❌ File not found: {COMMENTS_JSON_FILE}"))
            return
        
        comments_created = 0

        for comment_dict in comments_data:
            post_id = comment_dict.pop("postId", None)

            if post_id is None:
                self.stderr.write(self.style.WARNING(f"⚠️ Skipping comment with missing postId: {comment_dict}"))
                continue
            
            try:
                post = Post.objects.get(id=post_id)
            except Post.DoesNotExist:
                self.stderr.write(self.style.WARNING(f"⚠️ Skipping comment {comment_dict['body'][:30]}... (Post ID {post_id} not found)"))
                continue

            # Create comment
            comment, created = Comment.objects.get_or_create(
                post=post,
                name=comment_dict["name"],
                email=comment_dict["email"],
                body=comment_dict["body"],
            )
            if created:
                comments_created += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Imported {comments_created} comments successfully!"))
