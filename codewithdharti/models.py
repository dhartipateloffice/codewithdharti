from django.db import models

class Langdb(models.Model):
    """Python Django HTML CSS"""
    langname = models.CharField(max_length=200)  # Name of the language/framework (e.g., Python)
    slug = models.SlugField(unique=True)  # URL-friendly version of the title
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when updated

    def __str__(self):
        return self.langname

class Topicdb(models.Model):
    """Python - DSA,CLASS,STRING,CONDITION,FEATURE,NEWFEATURE,BASIC"""
    langname = models.ForeignKey(Langdb, related_name='topics', on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)  # Name of the topic (e.g., Python Tuples)
    slug = models.SlugField(unique=True)  # URL-friendly version of the title
    topic_content = models.TextField(blank=True, null=True)  # Main content for the topic
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when updated

    def __str__(self):
        return self.topic

class Subtopicdb(models.Model):
    """DSA - list tuple array"""
    topic = models.ForeignKey(Topicdb, related_name='subtopics', on_delete=models.CASCADE)
    subtopic = models.CharField(max_length=200)  # Name of the subtopic (e.g., Access Tuple)
    slug = models.SlugField(unique=True)  # URL-friendly version of the title
    sub_content = models.TextField(blank=True, null=True)  # Main content for the subtopic
    color = models.CharField(max_length=7,blank=True, null=True) 
    extranote = models.CharField(blank=True, null=True,max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when updated

    def __str__(self):
        return f"{self.topic.topic} - {self.subtopic} "

class Nanotopicdb(models.Model):
    """list- syntax access delete"""
    subtopic = models.ForeignKey(Subtopicdb, related_name='nanotopics', on_delete=models.CASCADE)
    nanotopic = models.CharField(max_length=200)
    # slug = models.SlugField(unique=True)  # URL-friendly version of the title
    # code_content = models.TextField(blank=True, null=True, help_text="Code snippet content")
    image = models.ImageField(upload_to='images/', blank=True, null=True, help_text="Optional Output img related to code")
    nano_content = models.TextField(blank=True, null=True)  
    # color = models.CharField(max_length=7,blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when updated

    def __str__(self):
        return self.nanotopic

class CodeContent(models.Model):
    """Stores individual code blocks related to a nanotopic."""
    nanotopic = models.ForeignKey(Nanotopicdb, related_name='code_blocks', on_delete=models.CASCADE)
    code_content = models.TextField(help_text="Content of the code block")  # Store each individual code block
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created

    def __str__(self):
        return f"Code block for {self.nanotopic.nanotopic}"


class Codeideadb(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the code snippet")
    image = models.ImageField(upload_to='images/', blank=True, null=True, help_text="Optional image related to code")
    content = models.TextField(blank=True, null=True, help_text="Optional content related to code")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    # dhartipatel - super user pass