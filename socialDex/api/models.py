from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from api.utils import send_transaction
import hashlib

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    hash = models.CharField(max_length=32, default=None, null=True)
    tx_id = models.CharField(max_length=66, default=None, null=True)

    def write_on_chain(self):
        self.hash = hashlib.sha256(self.content.encode('utf-8')).hexdigest()
        self.tx_id = send_transaction(self.hash)
        self.save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()





