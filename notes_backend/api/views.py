from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

# PUBLIC_INTERFACE
@api_view(['GET'])
def health(request):
    """Health check endpoint for server status."""
    return Response({"message": "Server is up!"})

# PUBLIC_INTERFACE
class NoteListCreateView(generics.ListCreateAPIView):
    """
    API endpoint for listing, searching/filtering, and creating notes.

    get:
    Returns a list of all notes. You may filter by `title` or search by keyword in title/content using the `search` query parameter.

    post:
    Create a new note. Requires 'title' and (optionally) 'content'.
    """
    serializer_class = NoteSerializer
    queryset = Note.objects.all().order_by('-updated_at')
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)
        # DRF SearchFilter handles `?search=keyword`
        return queryset

# PUBLIC_INTERFACE
class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating or deleting a note by ID.

    get:
    Retrieve details for a single note.

    put:
    Update all fields of the note.

    patch:
    Partially update fields in the note.

    delete:
    Delete the note.
    """
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
