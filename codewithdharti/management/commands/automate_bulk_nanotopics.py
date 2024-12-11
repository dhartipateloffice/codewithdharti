from django.core.management.base import BaseCommand
from ...models import Nanotopicdb, Subtopicdb, CodeContent
import os
import re

class Command(BaseCommand):
    help = 'Automate bulk nanotopics creation'

    def read_functions_from_file(self, file_path):
        """Read Python code from a file and extract function definitions."""
        if not os.path.exists(file_path):
            print(f"Error: The file {file_path} does not exist.")  # Debugging output
            return [("Error", f"# Error: The file {file_path} does not exist.")]
        
        with open(file_path, 'r') as file:
            code = file.read()

        functions = []
        function_pattern = re.compile(r"(def .+?\(.*?\):[\s\S]*?)(?=\n\w|\Z)", re.MULTILINE)
        for match in function_pattern.finditer(code):
            function_code = match.group(1)  # Entire function definition + body
            functions.append(function_code)
        
        return functions

    def format_nanotopic_name(self, nanotopic_name):
        """Format nanotopic names to proper title case with spaces."""
        # Replace underscores with spaces and capitalize each word
        formatted_name = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', nanotopic_name)
        formatted_name = formatted_name.replace('_', ' ').title()
        return formatted_name

    def handle(self, *args, **kwargs):
        """Handles the creation of nanotopics from code files."""
        code_files = [

            # #get id using shell
            # >>> subtopic = Subtopicdb.objects.get(id=34) 
            # >>> print(subtopic)
            # Play with DSA - Set

            # 'E:/Projects/website/learncode/codewithdharti/code_files/list.py',  
            # 'E:/Projects/website/learncode/codewithdharti/code_files/tuple.py',  
            # 'E:/Projects/website/learncode/codewithdharti/code_files/set.py',  
            # 'E:/Projects/website/learncode/codewithdharti/code_files/dict.py',  
            # 'E:/Projects/website/learncode/codewithdharti/code_files/array.py',  

            # 'E:/Projects/website/learncode/codewithdharti/code_files/varname.py',  
            # 'E:/Projects/website/learncode/codewithdharti/code_files/type.py',  
            # 'E:/Projects/website/learncode/codewithdharti/code_files/userinput.py', 
            # 'E:/Projects/website/learncode/codewithdharti/code_files/numbers1.py', 
            # 'E:/Projects/website/learncode/codewithdharti/code_files/array.py', 
            # 'E:/Projects/website/learncode/codewithdharti/code_files/module.py', 
            # 'E:/Projects/website/learncode/codewithdharti/code_files/bool1.py', 

            # 'E:/Projects/website/learncode/codewithdharti/code_files/class.py', 
            # 'E:/Projects/website/learncode/codewithdharti/code_files/class_advance.py', 
            # 'E:/Projects/website/learncode/codewithdharti/code_files/inheritance.py', 
            # 'E:/Projects/website/learncode/codewithdharti/code_files/public_private_protected.py', 
            # 'E:/Projects/website/learncode/codewithdharti/code_files/polymorphism.py', 
            # 'E:/Projects/website/learncode/codewithdharti/code_files/overloading_overriding.py', 
            # 'E:/Projects/website/learncode/codewithdharti/code_files/functions.py', #17
            # 'E:/Projects/website/learncode/codewithdharti/code_files/decorators.py', 
            # 'E:/Projects/website/learncode/codewithdharti/code_files/generator.py', #19
            # 'E:/Projects/website/learncode/codewithdharti/code_files/lamda.py', #20
            # 'E:/Projects/website/learncode/codewithdharti/code_files/iterators.py', #21
            # 'E:/Projects/website/learncode/codewithdharti/code_files/scope.py', 

            # 'E:/Projects/website/learncode/codewithdharti/code_files/if_else.py', #23
            # 'E:/Projects/website/learncode/codewithdharti/code_files/try_catch.py', #24

            # 'E:/Projects/website/learncode/codewithdharti/code_files/datetime_1.py', #27
            # 'E:/Projects/website/learncode/codewithdharti/code_files/file_handling.py', #26
            # 'E:/Projects/website/learncode/codewithdharti/code_files/json1.py', 
            # 'E:/Projects/website/learncode/codewithdharti/code_files/math_1.py', #28

            # 'E:/Projects/website/learncode/codewithdharti/code_files/call_value_ref.py', #29
            # 'E:/Projects/website/learncode/codewithdharti/code_files/pickle1.py', #31
            # 'E:/Projects/website/learncode/codewithdharti/code_files/array.py', 

            'E:/Projects/website/learncode/codewithdharti/code_files/regex.py', #33
            # 'E:/Projects/website/learncode/codewithdharti/code_files/array.py', 
        ]

        nanotopics_data = []
        for file_path in code_files:
            functions = self.read_functions_from_file(file_path)
            for function_code in functions:
                function_name = re.match(r"def (\w+)\(", function_code)
                if function_name:
                    function_name = function_name.group(1)  # Extract the function name

                # Format nanotopic name (e.g., multiple_datatype -> Multiple Datatype)
                formatted_function_name = self.format_nanotopic_name(function_name)

                # Prepare data for Nanotopicdb and CodeContent
                nanotopics_data.append({
                    'subtopic_id': 33,  # Adjust according to the actual subtopic
                    'nanotopic': formatted_function_name,  # Use formatted name
                    'code_content': function_code,
                    'nano_content': f"This section covers the function {formatted_function_name}.",
                })

        # Bulk create the Nanotopicdb instances
        nanotopic_instances = []
        code_content_instances = []
        for data in nanotopics_data:
            try:
                subtopic = Subtopicdb.objects.get(id=data['subtopic_id'])
                
                # Check if the nanotopic already exists
                existing_nanotopic = Nanotopicdb.objects.filter(subtopic=subtopic, nanotopic=data['nanotopic']).first()
                if existing_nanotopic:
                    self.stdout.write(self.style.SUCCESS(f"Skipping creation of existing nanotopic: {data['nanotopic']}"))
                    continue  # Skip if the nanotopic already exists

                # Create Nanotopicdb instance without code_content directly
                nanotopic_instance = Nanotopicdb(
                    subtopic=subtopic,
                    nanotopic=data['nanotopic'],
                    nano_content=data['nano_content'],
                )
                nanotopic_instances.append(nanotopic_instance)

                # Create CodeContent instance for each nanotopic
                code_content_instance = CodeContent(
                    nanotopic=nanotopic_instance,  # Link to the newly created nanotopic
                    code_content=data['code_content']
                )
                code_content_instances.append(code_content_instance)

            except Subtopicdb.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Subtopic with ID {data['subtopic_id']} does not exist."))
                continue

        # Save Nanotopicdb and CodeContent instances
        if nanotopic_instances:
            Nanotopicdb.objects.bulk_create(nanotopic_instances)
            self.stdout.write(self.style.SUCCESS(f"Successfully added {len(nanotopic_instances)} new nanotopics."))

        if code_content_instances:
            CodeContent.objects.bulk_create(code_content_instances)
            self.stdout.write(self.style.SUCCESS(f"Successfully added {len(code_content_instances)} new code blocks."))
