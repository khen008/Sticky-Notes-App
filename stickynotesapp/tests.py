"""
Unit tests for the Sticky Notes application.

This module tests:
- Note model
- List view
- Create view
- Update view
- Delete view
"""

from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteModelTest(TestCase):
    """
    Test cases for the Note model.
    """

    def setUp(self):
        """
        Create a sample note before each test runs.
        """
        Note.objects.create(
            title="Test Note",
            content="This is a test note."
        )

    def test_note_title(self):
        """
        Ensure the note title is saved correctly.
        """
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, "Test Note")

    def test_note_content(self):
        """
        Ensure the note content is saved correctly.
        """
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, "This is a test note.")


class NoteViewTest(TestCase):
    """
    Test cases for note views.
    """

    def setUp(self):
        """
        Create a note for testing views.
        """
        Note.objects.create(
            title="View Test Note",
            content="Testing views."
        )

    def test_note_list_view(self):
        """
        Test that the notes list page loads correctly.
        """
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Test Note")

    def test_create_note_view(self):
        """
        Test creating a new note.
        """
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'Created in test'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 2)

    def test_update_note_view(self):
        """
        Test updating an existing note.
        """
        note = Note.objects.get(id=1)

        response = self.client.post(reverse('note_update', args=[note.id]), {
            'title': 'Updated Note',
            'content': 'Updated content'
        })

        self.assertEqual(response.status_code, 302)

        note.refresh_from_db()
        self.assertEqual(note.title, 'Updated Note')

    def test_delete_note_view(self):
        """
        Test deleting a note.
        """
        note = Note.objects.get(id=1)

        response = self.client.post(reverse('note_delete', args=[note.id]))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)