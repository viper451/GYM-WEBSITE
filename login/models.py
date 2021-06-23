from django.db import models
from django.contrib.auth.models import User

# Create your models here.





class Fit(models.Model):
    type=(
    ('MALE','MALE'),  
		('FEMALE','FEMALE'), 
		('OTHERS','OTHERS'), 
	)

   
  
    username =models.ForeignKey(User, on_delete=models.SET_NULL,max_length=30,null=True)
    gender=models.CharField(max_length=20,choices=type,default='MALE',null=False)
    age=models.IntegerField()
    flexibility=models.IntegerField()
    fitness=models.IntegerField()
    aerobic=models.IntegerField()


    def __str__(self):
       return str(self.username)

class Registeration(models.Model):
  type=(
    ('MALE','MALE'),   
		('FEMALE','FEMALE'), 
		('OTHERS','OTHERS'), 
	)
  payment_options = (
		('G-Pay', 'G-Pay'),
		('PayPal', 'PayPal'),
		('Paytm', 'Paytm'),
		)
  offertype = (
		('Gold','Gold  ₹5999'),
		('Silver','Silver  ₹3999'),
		('Bronze','Bronze  ₹1999'),
		)
  username = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="Register", null=True,blank=True)
  firstname=models.CharField(max_length=20,null=False)
  lastname=models.CharField(max_length=20,null=False)
  age=models.IntegerField(null=False)
  gender=models.CharField(max_length=20,choices=type,default='MALE',null=False)
  phonenumber=models.IntegerField(null=False)
  offer=models.CharField(max_length=20,choices=offertype,default='Gold  ₹1999',null=False)
  modeofpayment=models.CharField(max_length=20,choices=payment_options,default='G-Pay',null=False)


  def __str__(self):
       return str(self.firstname)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text       




  



