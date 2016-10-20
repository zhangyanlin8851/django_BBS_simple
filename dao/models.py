from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    url = models.CharField(max_length=255)
    # img = models.ImageField(null=True, blank=True,)
    create_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('Userinfo')


class Userinfo(models.Model):
    username = models.CharField(max_length=20,db_index=True)
    passwd = models.CharField(max_length=20)



