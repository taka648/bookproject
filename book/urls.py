# bookアプリ[book]を作成[~/ohashi_book/bookproject$ python manage.py startapp book]ではurls.py作成されない
from django.urls import path  # リスト1:コード追加
from . import views           # リスト1:コード追加

urlpatterns = [ 
    path('', views.index_view, name='index'), # リスト1:コード追加
    path('book/', views.ListBookView.as_view(), name='list-book'), # リスト7:コード追加
    path('book/<int:pk>/detail/', views.DetailBookView.as_view(), name='detail-book'), # リスト8:コード追加
    path('book/create/', views.CreateBookView.as_view(), name='create-book'), # リスト8:コード追加
    path('book/<int:pk>/delete/', views.DeleteBookView.as_view(), name='delete-book'), # リスト1:コード追加
    path('book/<int:pk>/update/', views.UpdateBookView.as_view(), name='update-book'), # リスト1:コード追加
    # path('logout/', views.logout_view, name='logout'), # リスト3:コード削除
    path('book/<int:book_id>/review/', views.CreateReviewView.as_view(), name='review'), # リスト1:コード追加
] 
