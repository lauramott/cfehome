

from rest_framework import generics
from facescan.models import Item
from .serializers import BlogPostSerializer


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field        = 'slug' # pk or id...
    serializer_class    = BlogPostSerializer

    def get_queryset(self):
        return Item.objects.all()



