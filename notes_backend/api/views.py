from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

from .models import Note
from .serializers import NoteSerializer


@api_view(["GET"])
def health(request):
    """
    Health check endpoint.

    Returns:
        200 OK with a simple message payload to indicate the server is running.
    """
    return Response({"message": "Server is up!"})


# PUBLIC_INTERFACE
class NoteViewSet(viewsets.ModelViewSet):
    """ViewSet providing CRUD operations for Note model."""
    queryset = Note.objects.all().order_by("-created_at")
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id="listNotes",
        operation_summary="List notes",
        operation_description="Retrieve a paginated list of notes ordered by newest first.",
        responses={200: NoteSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="createNote",
        operation_summary="Create a note",
        operation_description="Create a new note with a title and content.",
        request_body=NoteSerializer,
        responses={201: NoteSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="retrieveNote",
        operation_summary="Retrieve a note",
        operation_description="Retrieve a single note by its ID.",
        responses={200: NoteSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="updateNote",
        operation_summary="Update a note",
        operation_description="Replace a note's data by its ID.",
        request_body=NoteSerializer,
        responses={200: NoteSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="partialUpdateNote",
        operation_summary="Partially update a note",
        operation_description="Partially update fields of a note by its ID.",
        request_body=NoteSerializer,
        responses={200: NoteSerializer()}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="deleteNote",
        operation_summary="Delete a note",
        operation_description="Delete a note by its ID.",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
