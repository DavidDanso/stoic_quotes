from django.db import models
import uuid

# Create your models here.
class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    updated_time_stamp = models.DateTimeField(auto_now=True)
    created_time_stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    # display quote with title in the database
    def __str__(self):
        return self.quote

    # display new quotes first
    class Meta:
        ordering = ['-updated_time_stamp']
