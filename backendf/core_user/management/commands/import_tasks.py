import json
from django.core.management.base import BaseCommand
from core_task.models import Task
from core_user.models import User

# Update this path to match the correct location of tasks.json
TASKS_JSON_FILE = "data/tasks.json"  # Adjust if needed

class Command(BaseCommand):
    help = "Import tasks from a JSON file."

    def handle(self, *args, **options):
        try:
            with open(TASKS_JSON_FILE, "r") as f:
                tasks_data = json.load(f)
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"❌ File not found: {TASKS_JSON_FILE}"))
            return

        tasks_created = 0

        for task_dict in tasks_data:
            user_id = task_dict.pop("userId")  # Get userId from JSON

            try:
                user = User.objects.get(id=user_id)  # Ensure user exists
            except User.DoesNotExist:
                self.stderr.write(self.style.WARNING(f"⚠️ Skipping task {task_dict['id']}: User {user_id} not found."))
                continue

            # Create task with the correct User instance
            task, created = Task.objects.get_or_create(
                id=task_dict["id"],
                user=user,
                title=task_dict["title"],
                completed=task_dict["completed"]
            )

            if created:
                tasks_created += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Imported {tasks_created} tasks successfully!"))
