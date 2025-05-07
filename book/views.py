from django.contrib.auth.mixins import LoginRequiredMixin # リスト1:コード追加
from django.core.exceptions import PermissionDenied # リスト2:コード追加

from django.shortcuts import render, redirect # リスト2:コード追加
# from django.contrib.auth import logout        # リスト4:コード削除

# from django.urls import reverse_lazy # リスト6:コード追加
from django.urls import reverse, reverse_lazy # リスト14:コード追加
from django.views.generic import (
  ListView, 
  DetailView, 
  CreateView, 
  DeleteView, 
  UpdateView, # リスト2:コード追加
)

from django.db.models import Avg # リスト2:コード追加

from .models import Book, Review # リスト4:コード修正

from django.core.paginator import Paginator # リスト1:コード追加
from .consts import ITEM_PER_PAGE # リスト1:コード追加


# class ListBookView(ListView):             # リスト2:コード追加
class ListBookView(LoginRequiredMixin, ListView): # リスト1:コード追加
  template_name = 'book/book_list.html'   # リスト2:コード追加 
  model = Book                            # リスト2:コード追加

  paginate_by = ITEM_PER_PAGE             # リスト6:コード追加

# class DetailBookView(DetailView): # リスト2:コード追加
class DetailBookView(LoginRequiredMixin, DetailView): # リスト2:コード追加
  template_name = 'book/book_detail.html' 
  model= Book 

# class CreateBookView(CreateView): # リスト2:コード追加
class CreateBookView(LoginRequiredMixin, CreateView): # リスト2:コード追加
  template_name = 'book/book_create.html' 
  model= Book 
  # fields = ('title', 'text', 'category') # リスト4:コード追加
  fields = ('title', 'text', 'category', 'thumbnail') # リスト8:コード追加
  success_url = reverse_lazy('list-book') # リスト6:コード追加

  def form_valid(self, form): # リスト5:コード追加
    form.instance.user = self.request.user

    return super().form_valid(form)



# class UpdateBookView(UpdateView): # リスト2:コード追加
class UpdateBookView(LoginRequiredMixin, UpdateView): # リスト2:コード追加
  model= Book 
  # fields = ('title', 'text', 'category')
  fields = ('title', 'text', 'category', 'thumbnail') # リスト8:コード追加
  template_name = 'book/book_update.html' 
  # success_url = reverse_lazy('list-book') # リスト3:コード削除

  def get_object(self, queryset=None): # リスト2:コード追加
    obj = super().get_object(queryset)

    if obj.user != self.request.user:
      raise PermissionDenied

    return obj

  def get_success_url(self): # リスト3:コード追加
    return reverse('detail-book', kwargs={'pk':self.object.id})


# class DeleteBookView(DeleteView): # リスト2:コード追加
class DeleteBookView(LoginRequiredMixin, DeleteView): # リスト2:コード追加
  template_name = 'book/book_confirm_delete.html' 
  model= Book 
  success_url = reverse_lazy('list-book') 

  def get_object(self, queryset=None): # リスト4:コード追加
    obj = super().get_object(queryset)

    if obj.user != self.request.user:
      raise PermissionDenied

    return obj 
    


def index_view(request): 
  # object_list = Book.objects.order_by('category') # リスト3:コード追加
  # object_list = Book.objects.order_by('-id') # リスト1:コード修正
  object_list = Book.objects.all() # リスト1:コード修正

  ranking_list = Book.objects.annotate(avg_rating=Avg('review__rate')).order_by(
    '-avg_rating'
  ) # リスト2:コード追加


  paginator = Paginator(ranking_list, ITEM_PER_PAGE) # リスト1:コード追加
  page_number = request.GET.get('page',1) # リスト1:コード追加
  page_obj = paginator.page(page_number) # リスト1:コード追加


  # query = request.GET ['number'] # リスト3、2:コード追加
  # print(query)                   # リスト3、2:コード追加


  return render(
    request, 
    'book/index.html', 
    {
      'object_list':object_list,
      'ranking_list':ranking_list,
      'page_obj':page_obj
    },
  ) # リスト1:コード追加



# def logout_view(request): # リスト4:コード削除
#   logout(request)
#   return redirect('index') # リスト5:コード変更
#   # return render(request, 'book/index.html', {}) # リスト4:コード変更

# class CreateReviewView(CreateView): # リスト4:コード追加
class CreateReviewView(LoginRequiredMixin, CreateView): # リスト2:コード追加
  model = Review
  fields = ('book','title','text','rate')
  template_name = 'book/review_form.html'

  def get_context_data(self, **kwargs): # リスト6:コード追加
    context = super().get_context_data(**kwargs)
    context['book'] = Book.objects.get(pk=self.kwargs['book_id'])  # リスト8:コード追加
    # print(context) # リスト7:コード追加
    return context

  def form_valid(self, form): # リスト13:コード追加
    form.instance.user = self.request.user
    return super().form_valid(form)

  def get_success_url(self): # リスト14:コード追加
    return reverse('deta.il-book', kwargs={'pk':self.object.book.id}) 
