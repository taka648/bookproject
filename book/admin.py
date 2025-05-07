from django.contrib import admin
# from .models import SampleModel  # リスト5:コード追加
from .models import Book, Review # リスト11:コード追加

# admin.site.register(SampleModel) # リスト5:コード追加
admin.site.register(Book) # リスト5:コード追加
admin.site.register(Review) # リスト11::コード追加

