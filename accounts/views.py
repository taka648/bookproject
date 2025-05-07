from django.shortcuts import render

from django.contrib.auth.models import User # リスト8:コード追加
from django.urls import reverse_lazy        # リスト8:コード追加
from django.views.generic import CreateView # リスト8:コード追加

from .forms import SignupForm # リスト8:コード追加

class SignupView(CreateView):            # リスト8:コード追加
  model = User                          
  form_class = SignupForm               
  template_name = 'accounts/signup.html'
  success_url = reverse_lazy('index')   
