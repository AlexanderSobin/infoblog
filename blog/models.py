from django.contrib.auth.models import User
from django.db import models

SHORT_TEXT_LEN = 100


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User)


    def __str__(self):
        return self.title


    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=11)
    question = models.CharField(max_length=500)


class Comments(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()


    def __str__(self):
        return self.author