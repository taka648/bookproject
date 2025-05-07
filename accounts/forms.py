# [accounts/urls.py or views.py]form_classでSignupFormというフォームを指定している
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

# SignupFonnを定義する
class SignupForm(UserCreationForm): 
  class Meta:
    model = User
    fields = ('username',)
