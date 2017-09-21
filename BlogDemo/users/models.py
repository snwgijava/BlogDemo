from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    nickname = models.CharField(verbose_name='昵称',max_length=50, blank=True)
    user = models.OneToOneField(User)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username