from django.contrib import admin
from .models import *
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,               {'fields': ['question_text']}),
                ('Date information', {'fields': ['pub_date']})]
    list_display = ('question_text', 'pub_date')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
