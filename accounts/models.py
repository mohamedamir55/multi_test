from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField( max_length=15)
    address1=models.TextField()
    address2=models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profil(sender,instance,created, **kwargs):
    if created :
        Profil.objects.create(user=instance)
    

    
