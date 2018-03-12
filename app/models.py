from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user 			= models.OneToOneField(User, on_delete=models.CASCADE)
    descricao 		= models.TextField(max_length=500, blank=True)
    cidade 			= models.CharField(max_length=30, blank=True)
    estado 			= models.CharField(max_length=2, blank=True)
    dt_nascimento 	= models.DateField(null=True, blank=True)
    foto_perfil     = models.FileField(upload_to='perfil/', blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Mensagem(models.Model):
    destinatario	= models.ForeignKey(User, on_delete=models.CASCADE)
    remetente  		= models.CharField(max_length=30, blank=True)    
    assunto         = models.CharField(max_length=30, blank=True)
    mensagem   		= models.TextField(max_length=500, blank=True)
    dt_mensagem 	= models.DateTimeField(null=True, blank=True)
    lida            = models.BooleanField(default=False)

    def Lida(self, param):
        self.lida = param
        self.save()

    def __str__(self):
        return self.assunto