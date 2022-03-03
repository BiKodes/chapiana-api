import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                    'twitter': 'twitter', 'email': 'email'}

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auth_provider = models.CharField(max_length=250, blank=False, null=False, 
                                        default=AUTH_PROVIDERS.get('email'))

    def __str__(self):
        return self.username 

    


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
