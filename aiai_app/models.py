from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CATEGORY = (('man', '男性'), ('woman', '女性'), ('other', 'その他'))

# ユーザーアカウントのモデルクラス
class Account(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 追加フィールド
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    account_image = models.ImageField(upload_to="profile_pics",blank=True)
    category = models.CharField(
        max_length=100,
        choices = CATEGORY,
    )
    area = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

class Connection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name = 'following', blank =True)

    def __str__(self):
        return self.user.username