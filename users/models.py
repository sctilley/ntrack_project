from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recentFormat = models.ForeignKey('base.MtgFormat', null=True, on_delete=models.CASCADE)
    recentDeck = models.ForeignKey('base.Deck', null=True, on_delete=models.CASCADE)
    mtgoUserName = models.CharField(null=True, max_length=80)

    def __str__(self):
        return f'{self.user.username} Profile'