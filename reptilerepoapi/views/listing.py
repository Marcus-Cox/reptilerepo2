""" Module for Menu Items requests """
from cgi import print_exception
from turtle import title
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from reptilerepoapi.models import Listing, species
from reptilerepoapi.models import Lister
from reptilerepoapi.models import Species


class ListingView(ViewSet):
    """ Menu Items Viewset """

    def retrieve(self, request, pk):
        """ Handle a GET request for a menu item """
        try:
            listing = Listing.objects.get(pk=pk)
            serializer = ListingSerializer(listing)
            return Response(serializer.data)
        except Listing.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """ Handle a GET request for all of the menu items """
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)

    def create(self, request):
        """ Handle a POST request for a menu item """
        # incoming_user = request.auth.user
        lister  = Lister.objects.get(user=request.auth.user)
        species = Species.objects.get(pk=request.data["species"])
        
        new_listing = Listing.objects.create(
            sex=request.data["sex"],
            morph=request.data["morph"],
            age=request.data["age"],
            listing_date=request.data["listing_date"],
            hatch_date=request.data.get("hatch_date"),
            diet=request.data.get("diet"),
            price=request.data.get("price"),
            lister=lister,
            species=species
        )
        serializer = ListingSerializer(new_listing)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """ Handles a PUT request for a menu item """
        editing_listing = Listing.objects.get(pk=pk)

        editing_listing.sex = request.data["sex"]
        editing_listing.morph = request.data["morph"]
        editing_listing.age = request.data["age"]
        editing_listing.listing_date = request.data["listing_date"]
        editing_listing.hatch_date = request.data.get["hatch_date"]
        editing_listing.diet=request.data.get["diet"]
        species= Species.objects.get(pk=request.data["species"])
        editing_listing.species=request.data.get["species"]
        editing_listing.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """ Handles a DELETE request for a menu item """
        try:
            listing = Listing.objects.get(pk=pk)
            listing.delete()
        except Listing.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ListingSerializer(serializers.ModelSerializer):
    """ JSON serializer for menu items """
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
