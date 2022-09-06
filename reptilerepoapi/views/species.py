from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from reptilerepoapi.models import Species

class SpeciesView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        species = Species.objects.get(pk=pk)
        serializer = SpeciesSerializer(species)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        species = Species.objects.all()
        serializer = SpeciesSerializer(species, many=True)
        return Response(serializer.data)


class SpeciesSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Species
        fields = ('id', 'species')
        depth = 2
