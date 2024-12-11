from django.core.management.base import BaseCommand
from ...models import Langdb,Topicdb,Subtopicdb
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Add or update topics and subtopics'

    def handle(self, *args, **kwargs):
        # Define your topics and subtopics here
        topics_data = {
            "Play with Basics": [
                "Variable", "Type", "UserInput", "Number", "Operator", "Module", "Bool"
            ],
            "Play with Class": [
                "Class", "Class Advance", "Inheritance", "PPP", "Polymorphism", "Overloading and Overriding",
                "Functions", "Decorator", "Generator", "Lambda", "Iterators", "Scope"
            ],
            "Play with Conditions": [
                "IfElse", "TryCatch"
            ],
            "Play with Features": [
                "JSON", "FileHandling", "Datetime", "Math"
            ],
            "Play with New Features": [
                "Call by Value and Reference", "PEP-8", "Pickle"
            ],
            "Play with String": [
                "Manipulation in Strings", "Regex"
            ]
        }

        # Iterate through topics and subtopics
        for topic_name, subtopics in topics_data.items():
            topic_slug = slugify(topic_name)

            # Check if the topic exists, or create it if not
            topic, created = Topicdb.objects.get_or_create(slug=topic_slug, defaults={'name': topic_name})

            if created:
                self.stdout.write(self.style.SUCCESS(f"Created new topic: {topic_name}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Topic already exists: {topic_name}"))

            # Add or update subtopics for this topic
            for subtopic_name in subtopics:
                subtopic_slug = slugify(subtopic_name)

                # Check if subtopic exists, or create it if not
                subtopic, subtopic_created = Subtopicdb.objects.get_or_create(
                    slug=subtopic_slug, 
                    topic=topic, 
                    defaults={'name': subtopic_name}
                )

                if subtopic_created:
                    self.stdout.write(self.style.SUCCESS(f"Created new subtopic: {subtopic_name}"))
                else:
                    self.stdout.write(self.style.SUCCESS(f"Subtopic already exists: {subtopic_name}"))
