from django.db import models
import uuid
# from ckeditor.fields import RichTextField

class Gifts(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,unique=True,editable=False)
    creator=models.CharField(max_length=255,blank=False,null=False)
    img=models.ImageField(upload_to='gifts/images')
    description=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Gift'
        verbose_name_plural='Gifts'
        
    def __str__(self):
        return str(self.id)


class Birthday(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,unique=True,editable=False)
    age=models.IntegerField(null=False,blank=False)
    creator=models.CharField(max_length=255,blank=False,null=False)
    img=models.ImageField(upload_to='gifts/birthday/images')
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Birthday'
        verbose_name_plural='Birthdays'
        
    def __str__(self):
        return str(self.id)
