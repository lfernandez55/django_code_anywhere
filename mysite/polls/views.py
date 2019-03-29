# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, Foo, Baz, Person, Email, Company, Employee


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

#############################################################################
#make sure to import foo above
def foo(request, foo_id):
    try:
        #the below is outputted to the console
        print ('debug', foo_id)
        foo = Foo.objects.get(pk=foo_id)
    except Foo.DoesNotExist:
        raise Http404("Foo does not exist")
    return render(request, 'polls/foo.html', {'foo': foo})
  
class FooListView(generic.ListView):
    model = Foo
    #template inferred (foo_list.html)

class FooDetailView(generic.DetailView):
    model = Foo
    #template inferred  (foo_detail.html)
    
    
def baz(request, question_id):
    #response = "You're looking at the results of question %s."
    response = question_id
    q = Question.objects.get(pk=question_id)
    response = q.was_published_recently()
    if q.was_published_recently() == False:
      response = "Was NOT published recently"
    else:
      response = "WAS published recently "
    #return HttpResponse('debug', question_id)
    #return HttpResponse(response % question_id)
    return HttpResponse(response)
    
def baz2(request):
    mystring = ""
    for q in Baz.my_custom_sql():
      print(q) 
      print(type(q))
      mystring = mystring + "<br>" + str(q)
    return HttpResponse(mystring)
  
def users(request):
    #mystring = Person.objects.get(id=1).password_text
    #mystring = 'boo'
    #e = Person.objects.get(id=1)
    #mystring = e.email_text
    #mystring = Question.objects.filter(choice__choice_text__isnull=False).distinct()
    #mystring = Question.objects.select_related()
    mystring = Person.objects.all().values('id','first_name_text','email')
    #filter(first_name_text='Luke').select_related('email_text')
    print(mystring)
    return HttpResponse(mystring)
  
class UserListView(generic.ListView):
    model = Person
    #template inferred (person_list.html)
  
def emails(request):
    mystring = 'goo'
    return HttpResponse(mystring)
  
def employees(request):
    employees = Employee.objects.all().values('id','name','company__name','company__abbrev')
    #template_name = 'polls/employees.html'
    #return HttpResponse(employees)
    context = {'employees': employees}
    return render(request, 'polls/employees.html', context)
#############################################################################    

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        #         response = "Votes %s."
        #         return HttpResponse(response % selected_choice.votes)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        #return render(request, 'polls/results.html', {'question': question})