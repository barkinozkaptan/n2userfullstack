from django.db import connection
from django.conf import settings

def reset_user_id_sequence():
    """
    Resets the ID sequence for the User table safely.
    Only works in PostgreSQL.
    """
    if 'postgresql' not in settings.DATABASES['default']['ENGINE']:
        print("Skipping reset_user_id_sequence: Not using PostgreSQL.")
        return

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT setval('core_user_id_seq', COALESCE((SELECT MAX(id) FROM core_user), 1));
        """)
