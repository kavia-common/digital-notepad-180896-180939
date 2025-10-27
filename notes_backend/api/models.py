from django.db import models


class Note(models.Model):
    """
    Note model representing a simple note with a title and content.

    Fields:
    - title: Short title for the note.
    - content: Full text content of the note.
    - created_at: Timestamp when the note was created.
    - updated_at: Timestamp when the note was last updated.
    """
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id}: {self.title[:50]}"
