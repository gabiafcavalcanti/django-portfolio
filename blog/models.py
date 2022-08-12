from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = RichTextField()
    texto = RichTextUploadingField()
    categoria = models.SlugField()
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.titulo

    