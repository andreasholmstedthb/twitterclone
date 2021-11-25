from django.db import models
from useraccounts.models import UserAccount

class Tweet(models.Model):
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, null=False)
    def __str__(self):
        return self.user_account.user.username
