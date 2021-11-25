from django.db import models
from django.contrib.auth.models import User

# User account model, the follow refers to its own class, but only one way, since its non symmetrical.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_account")
    follows = models.ManyToManyField('self', blank=True, symmetrical=False)
    def __str__(self):
        return self.user.username
