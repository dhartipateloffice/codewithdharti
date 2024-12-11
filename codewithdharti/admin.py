from django.contrib import admin

from codewithdharti.models import Langdb,Topicdb,Subtopicdb,Nanotopicdb,CodeContent,Codeideadb

admin.site.register(Langdb)
admin.site.register(Topicdb)
admin.site.register(Subtopicdb)
admin.site.register(Nanotopicdb)
admin.site.register(CodeContent)

@admin.register(Codeideadb)
class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)