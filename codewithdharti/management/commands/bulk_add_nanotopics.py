from django.core.management.base import BaseCommand
from ...models import Nanotopicdb, Subtopicdb
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Bulk add Nanotopicdb entries'

    def handle(self, *args, **kwargs):
        # Data to bulk add
        nanotopics_data = [
            {
                'subtopic_id': 1,  # Example: ID of the subtopic
                'nanotopic': 'Syntax Access Delete',
                'slug': 'syntax-access-delete',
                'code_content': '''
# Python Code
def example():
    return "Hello, World!"  # Simple function''',
                'nano_content': 'This section covers how to access and delete data in Python.',
                'image': 'media/images/img3.jpg',  # Provide relative path to the image
                'color': '#ff5733'
            },
            {
                'subtopic_id': 2,
                'nanotopic': 'List Operations',
                'slug': 'list-operations',
                'code_content': '''
# Python Code
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
                                    ''',
                'nano_content': 'This section covers how to work with lists in Python.',
                'image': 'E:/Projects/website/learncode/codewithdharti/static/images/ai.png',
                'color': '#33cc33'
            },
            # Add more entries as needed
        ]

        # Prepare the data for bulk insertion
        nanotopic_instances = []
        for data in nanotopics_data:
            try:
                # Get the Subtopicdb instance from the ID
                subtopic = Subtopicdb.objects.get(id=data['subtopic_id'])

                # Create a Nanotopicdb instance
                nanotopic_instance = Nanotopicdb(
                    subtopic=subtopic,
                    nanotopic=data['nanotopic'],
                    slug=slugify(data['slug']),
                    code_content=data['code_content'],
                    nano_content=data['nano_content'],
                    image=data['image'],
                    color=data['color']
                )
                nanotopic_instances.append(nanotopic_instance)

            except Subtopicdb.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Subtopic with ID {data['subtopic_id']} does not exist."))
                continue

        # Bulk create the Nanotopicdb instances
        Nanotopicdb.objects.bulk_create(nanotopic_instances)
        self.stdout.write(self.style.SUCCESS(f"Successfully added {len(nanotopic_instances)} nanotopics."))
