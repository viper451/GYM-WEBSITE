from django.http.response import Http404
from django.shortcuts import render
from django.db.models import Avg

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.contrib import  messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import JsonResponse

from .models import Question, Choice

# Create your views here.

def loginPage(request):
    if request.method == 'POST':
       username=request.POST.get('username')
       password=request.POST.get('password')

       user=authenticate(request,username=username,password=password)

       if user is not None:
           login(request,user) 
           return redirect('index')
       else:
           messages.info(request,"Username OR PASSWORD INCORRECT")
    return render(request,'login.html')

def registerPage(request):
	
     form=CreateUserForm()

     if request.method =='POST':
       form = CreateUserForm(request.POST)
       if form.is_valid():
          form.save()
          user =form.cleaned_data.get('username')
          
          messages.success(request,"ACCOUNT CREATED successfully of "+ user)
          return redirect('login')
		
     context = {'form':form}
     return render(request,'registeration.html',context)


@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')     

     
@login_required(login_url='login')
def index(request):
    user=request.user
    form = User.objects.filter(username=user)
    if request.method =='POST':
        if form.is_valid():
               form.save()   
        messages.success(request,"ALLOWEED")	
        return redirect('index')
    return render(request,'list.html')   


@login_required(login_url='login')     
def news(request):
    return render(request,'news.html')   

@login_required(login_url='login')
def overallrating(request):
    user=request.user
    
    #averager =Rate.objects.all().aggregate(Avg('rating'))
    return render(request,'rating.html')   


    


    
  #  averagerate=averager.rating
  


    



@login_required(login_url='login')
def membership(request):
    return render(request,'membership.html')

@login_required(login_url='login')
def creator(request):
    return render(request,'creator.html')

@login_required(login_url='login')
def trainer(request):
    return render(request,'trainer.html')


@login_required(login_url='login')
def fitness(request,pk):

    form=FitnessForm()
    if request.method =='POST':
        form = FitnessForm(request.POST)
        if form.is_valid():
          form.save()   
        messages.success(request,"ALLOWEED")
        return redirect('fitnessresult')
    #if not Fit:
    
      #flexibility1=Fit.objects.get()
      #print(flexibility1.flexibility)
     # print("flexibility =", flexibility1)
    #else:
   #     print("EMPTY QUERYSET")


    
    #user=User.objects.get(id=pk)
    #form = FitnessForm(instance=user)
    #print("form = ",form)
    #print("user = ",user)
    
    
    
    context={'form':form}
    return render(request,'fitness.html',context)
def formup(request):

    form=RegisterForm()
    if request.method =='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.instance.username = request.user
            form.save()
        checkup=Registeration.objects.filter() 
        checkup.update(username=request.user)
        messages.success(request,"ALLOWED")
        return redirect('index') 


    context={'form':form}       
    return render(request,'signupform.html',context)


@login_required(login_url='login')
def fitnessresult(request):
      
    allvalue=Fit.objects.last()
    flexibility=allvalue.flexibility
    aerobic=allvalue.aerobic
    fitness=allvalue.fitness
    age=allvalue.age
    if age>20 and age<50:
        age=int(3)
    else:
        age=int(7)

    total_value1=((flexibility+aerobic+fitness)/3)+age
    total_value=round(total_value1,2)
    left_value=100-total_value


    context={'flexibility':flexibility,'aerobic':aerobic,'fitness':fitness,'total_value':total_value,'left_value':left_value}

    return render(request,'fitnessresult.html',context)


@login_required(login_url='login')
def index1(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index1.html', context)



@login_required(login_url='login')
# Show specific question and choices
def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'detail.html', { 'question': question })



@login_required(login_url='login')
# Get question and display results
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'results.html', { 'question': question })




@login_required(login_url='login')
# Vote for a question choice
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))



@login_required(login_url='login')
def resultsData(request, obj):
    votedata = []

    question = Question.objects.get(id=obj)
    votes = question.choice_set.all()

    for i in votes:
        votedata.append({i.choice_text:i.votes})

    print(votedata)
    return JsonResponse(votedata, safe=False)





