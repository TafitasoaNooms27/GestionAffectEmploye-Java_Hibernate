import uuid
import datetime
from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=5, default="USER")
    fullname = models.CharField(max_length=32)
    email = models.EmailField(max_length=50)
    created_at = models.DateField(default=datetime.date.today)