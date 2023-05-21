from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profiles_pic')

    def __str__(self) -> str:
        return self.user.username + 'profile'
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.image.path)
        if img.width > 200 or img.height > 200:
            resize = (200,200)
            img.thumbnail(resize)
            img.save(self.image.path)
