from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'popularity', 'is_availabe']

class ChoiceAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('question',     {'fields': ['choice_text', 'votes']})
    # ]
    list_display = ['question', 'choice_text', 'votes']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)