# docs/management/commands/populate_langdb.py

from django.core.management.base import BaseCommand
from ...models import Langdb
                  # Path to the Python code file

class Command(BaseCommand):
    help = 'Populates the Langdb model with predefined data'

    def handle(self, *args, **kwargs):
        # Predefined data to insert into Langdb
        lang_data = [
            {"langname": "Python", "slug": "python"},
            {"langname": "AI", "slug": "ai"},
            {"langname": "Django", "slug": "django"},
            {"langname": "FastAPI", "slug": "fastapi"},
            {"langname": "Flask", "slug": "flask"},
            {"langname": "MongoDB", "slug": "mongodb"},
            {"langname": "MySQL", "slug": "mysql"},
            {"langname": "ORM", "slug": "orm"},
            {"langname": "Pattern", "slug": "pattern"},
            {"langname": "Practice", "slug": "practice"}
        ]
        
        # Add data to Langdb
        for lang in lang_data:
            Langdb.objects.get_or_create(
                langname=lang["langname"],
                slug=lang["slug"]
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Langdb with languages'))
