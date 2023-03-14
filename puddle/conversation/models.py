from django.db import models
from django.contrib.auth.models import User

from items.models import Item

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-modified_at']

class ConversationMessage(models.Model):
        conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
        content = models.TextField()
        created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)

