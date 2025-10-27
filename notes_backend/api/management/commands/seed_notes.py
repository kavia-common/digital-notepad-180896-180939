from django.core.management.base import BaseCommand
from api.models import Note


class Command(BaseCommand):
    help = "Seed the database with sample notes"

    # PUBLIC_INTERFACE
    def handle(self, *args, **options):
        """Seed command to create a few sample notes for testing."""
        samples = [
            {"title": "Welcome", "content": "This is your first note."},
            {"title": "Ideas", "content": "Write down your ideas here."},
        ]
        created = 0
        for s in samples:
            if not Note.objects.filter(title=s["title"]).exists():
                Note.objects.create(**s)
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Seeded {created} notes"))
