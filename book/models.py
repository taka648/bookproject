from django.db import models
from .consts import MAX_RATE # リスト2:コード追加

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)] # リスト2:コード追加

# class SampleModel(models.Model):           # リスト2:コード追加
#   title = models.CharField(max_length=100) # リスト2:コード追加
#   number = models.IntegerField()           # リスト2:コード追加

CATEGORY = (('business', 'ビジネス'), ('life', '生活'), ('other','その他')) # リスト3:コード追加

class Book(models.Model):                  # リスト3:コード追加
  title = models.CharField(max_length=100) 
  text = models.TextField()                
  # thumbnail = models.ImageField() # リスト1:コード追加
  thumbnail = models.ImageField(null=True, blank=True) # リスト2:コード追加
  category = models.CharField(             
    max_length=100,                        
    choices = CATEGORY                     
  )                                        

  user = models.ForeignKey('auth.User', on_delete=models.CASCADE) # リスト1:コード追加

  def __str__(self): 
    return self.title 

class Review(models.Model): # リスト2:コード追加
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  text = models.TextField()
  rate = models.IntegerField(choices=RATE_CHOICES)
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

  def __str__(self):
    return self.title

