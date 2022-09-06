from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from reptilerepoapi.models import Morph

class MorphView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        morph = Morph.objects.get(pk=pk)
        serializer = MorphSerializer(morph)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        morph = Morph.objects.all()
        serializer = MorphSerializer(morph, many=True)
        return Response(serializer.data)


class MorphSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Morph
        fields = ('id', 'Morph')
        depth = 2
