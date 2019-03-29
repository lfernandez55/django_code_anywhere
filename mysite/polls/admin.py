from django.contrib import admin
from .models import Choice, Question, Person, Email
# Register your models here.

# from .models import Question
# admin.site.register(Question)

# from .models import Choice
# admin.site.register(Choice)


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    
    list_display = ('question_text', 'pub_date', 'was_published_recently')
  
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)




from .models import Foo
admin.site.register(Foo)

from .models import Person
admin.site.register(Person)

from .models import Email
admin.site.register(Email)

from .models import Employee
admin.site.register(Employee)

from .models import Company
admin.site.register(Company)
