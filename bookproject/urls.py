from django.conf import settings           # リスト4:コード追加
from django.conf.urls.static import static # リスト4:コード追加
from django.contrib import admin 
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')), # リスト1:コード追加
    path('accounts/', include('accounts.urls')), # リスト2:コード変更
    path('', include('book.urls')),    # リスト1:コード追加
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # リスト4:コード追加
