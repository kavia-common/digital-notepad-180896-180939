from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class NotesApiTests(APITestCase):
    def test_health(self):
        url = reverse('Health')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, {"message": "Server is up!"})

    def test_notes_crud(self):
        # Create
        create_resp = self.client.post('/api/notes/', {"title": "First", "content": "Hello"}, format='json')
        self.assertEqual(create_resp.status_code, status.HTTP_201_CREATED)
        note_id = create_resp.data["id"]

        # List
        list_resp = self.client.get('/api/notes/')
        self.assertEqual(list_resp.status_code, status.HTTP_200_OK)
        self.assertTrue(any(n["id"] == note_id for n in list_resp.data))

        # Retrieve
        retrieve_resp = self.client.get(f'/api/notes/{note_id}/')
        self.assertEqual(retrieve_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(retrieve_resp.data["title"], "First")

        # Update (PUT)
        put_resp = self.client.put(f'/api/notes/{note_id}/', {"title": "Updated", "content": "World"}, format='json')
        self.assertEqual(put_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(put_resp.data["title"], "Updated")

        # Partial Update (PATCH)
        patch_resp = self.client.patch(f'/api/notes/{note_id}/', {"content": "Patched"}, format='json')
        self.assertEqual(patch_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_resp.data["content"], "Patched")

        # Delete
        del_resp = self.client.delete(f'/api/notes/{note_id}/')
        self.assertEqual(del_resp.status_code, status.HTTP_204_NO_CONTENT)
