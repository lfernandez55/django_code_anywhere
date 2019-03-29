import datetime

from django.db import models
from django.utils import timezone
from django.core import serializers

#used in raw sql below
from django.db import connection, transaction

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Foo(models.Model):
    foo_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.foo_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
      
      
class Baz(models.Model):
    baz_text = models.CharField(max_length=200)
    baz_sillyfield = models.CharField(max_length=200)
    baz_sillyfield2 = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.baz_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
      
    def my_custom_sql():
          for p in Question.objects.raw('SELECT id, question_text FROM polls_Question '):
            print(p)
          return Question.objects.raw('SELECT id, question_text FROM polls_Question ')


class Person(models.Model):
    first_name_text = models.CharField(max_length=200)
    last_name_text = models.CharField(max_length=200)
    login_text = models.CharField(max_length=200)
    password_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
#        from https://www.quora.com/What-is-the-use-of-__str__-in-python
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

    
class Email(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    email_text = models.CharField(max_length=200)
    
class Company(models.Model):
    name = models.CharField(max_length=60)
    abbrev = models.CharField(max_length=60)

class Employee(models.Model):
    name = models.CharField(max_length=60)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
