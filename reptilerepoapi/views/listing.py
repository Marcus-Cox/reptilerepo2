""" Module for Listing Items requests """
from cgi import print_exception
from turtle import title
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from reptilerepoapi.models import Listing
from reptilerepoapi.models import Lister
from reptilerepoapi.models import Species
from reptilerepoapi.models import Sex
from reptilerepoapi.models import Morph
from reptilerepoapi.models import Diet


class ListingView(ViewSet):
    """ Listing Items Viewset """

    def retrieve(self, request, pk):
        """ Handle a GET request for a Listing item """
        try:
            listing = Listing.objects.get(pk=pk)
            serializer = ListingSerializer(listing)
            return Response(serializer.data)
        except Listing.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """ Handle a GET request for all of the Listing items """
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)

    def create(self, request):
        """ Handle a POST request for a Listing item """
        # incoming_user = request.auth.user
        lister  = Lister.objects.get(user=request.auth.user)
        species = Species.objects.get(pk=request.data["species"])
        sex = Sex.objects.get(pk=request.data["sex"])
        morph = Morph.objects.get(pk=request.data["morph"])
        diet = Diet.objects.get(pk=request.data["diet"])
        
        
        new_listing = Listing.objects.create(
            sex=sex,
            morph=morph,
            age=request.data["age"],
            listing_date=request.data["listing_date"],
            hatch_date=request.data.get("hatch_date"),
            diet=diet,
            price=request.data.get("price"),
            lister=lister,
            species=species
        )
        serializer = ListingSerializer(new_listing)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """ Handles a PUT request for a Listing item """
        editing_listing = Listing.objects.get(pk=pk)

        editing_listing.sex = request.data["sex"]
        editing_listing.morph = request.data["morph"]
        editing_listing.age = request.data["age"]
        editing_listing.hatch_date = request.data.get("hatch_date")
        editing_listing.diet=request.data.get("diet")
        editing_listing.price=request.data.get("price")
        # species= Species.objects.get(pk=request.data["species"])
        # editing_listing.species=request.data.get("species")
        editing_listing.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """ Handles a DELETE request for a Listing item """
        try:
            listing = Listing.objects.get(pk=pk)
            listing.delete()
        except Listing.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ListingSerializer(serializers.ModelSerializer):
    """ JSON serializer for Listing items """
    class Meta:
        model = Listing
        fields = (
            'id',
            'sex',
            'morph',
            'age',
            'listing_date',
            'hatch_date',
            'diet',
            'price',
            'lister',
            'species')
