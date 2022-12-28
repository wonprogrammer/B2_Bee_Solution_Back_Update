from django.db import models
from users.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sended_message')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_message')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    delete_receiver = models.BooleanField(default=False)
    delete_sender = models.BooleanField(default=False)