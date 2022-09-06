from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from reptilerepoapi.models import Sex

class SexView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        sex = Sex.objects.get(pk=pk)
        serializer = SexSerializer(sex)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        sex = Sex.objects.all()
        serializer = SexSerializer(sex, many=True)
        return Response(serializer.data)


class SexSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Sex
        fields = ('id', 'sex')
        depth = 2
