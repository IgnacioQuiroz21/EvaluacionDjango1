from rest_framework import serializers
from combate.models import Anuncio

class AnuncioSerializer(serializers.ModelSerializer):

    class Meta:

        model = Anuncio

        fields = ['idAnuncio','nombre','descAnuncio']