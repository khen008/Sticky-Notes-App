from django.db import models


class Note(models.Model):
    """
    Represents a sticky note created by a user.

    Attributes:
        title (str): The title of the note.
        content (str): The content/body of the note.
        created_at (datetime): Date and time when the note was created.
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the title of the note."""
        return self.title