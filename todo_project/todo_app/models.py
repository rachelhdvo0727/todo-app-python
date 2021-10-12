# Django's user authentication system
from django.contrib.auth.models import User
# Import django's standard model
from django.db import models


class Todo(models.Model):
    # Use Django's User model
    # so multiple apps in the same Project share the same user model

    # Assign a user to the Todo model
    # user becomes a prop on the Todo model with the FK type
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Add a text field to our model
    text = models.CharField(max_length=200)

    # Add a status field to our model
    status = models.BooleanField(default=False)

    # Return a human-readble representation of the model
    # & tell the todos apart in the admin panel list view
    def __str__(self):
        return f"{self.text} - {self.status}"
