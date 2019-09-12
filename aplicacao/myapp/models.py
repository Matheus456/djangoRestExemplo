from django.db import models

# Create your models here.


class Music(models.Model):

    class Meta:

        db_table = 'music'

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()

    def __str__(self):
        return self.title

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    nick = models.CharField(max_length=200)
