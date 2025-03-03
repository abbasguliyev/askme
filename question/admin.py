from django.contrib import admin
from .models import Question, Answer, Tag

class AnswerAdmin(admin.StackedInline):
    list_display = ('answer', 'question', 'created_at')
    model = Answer

admin.site.register(Answer)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'user', 'tags')

    inlines = [AnswerAdmin]

    def tags(self, obj):
        html = ""

        for tag in obj.tag.all():
            html += tag.name + ","
        return html
admin.site.register(Question, QuestionAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Tag, TagAdmin)