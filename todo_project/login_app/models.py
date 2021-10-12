from django.db import models
from django.contrib.auth.models import User
from secrets import token_urlsafe

class PasswordResetRequest(models.Model):
    # ForeignKey links the PasswordResetRequest to the user
    # -> keep track of the history of password reset attempts
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Add a strong random sequence of characters that can safely be url encoded
    token = models.CharField(max_length=43, default=token_urlsafe)

    # Set time when the object is instantiated
    # created_timestamp is set once
    created_timestamp = models.DateTimeField(auto_now_add=True)

    # updated_timestamp is to be set every time the obj is saved
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.created_timestamp} - {self.updated_timestamp} - {self.token}'
