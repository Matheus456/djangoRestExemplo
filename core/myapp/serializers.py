from rest_framework import serializers
from .models import Music, Pessoa

class MusicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Music
        fields = '__all__'

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:

        model = Pessoa
        fields = '__all__'

    # Método create para salvar o usuário
    def create(self, validated_data):
        usuario = Pessoa(
            nome=validated_data['nome'],
            sobrenome=validated_data['sobrenome'],
            senha=validated_data['senha'],
            nick=validated_data['nick']
        )
        usuario.save()
        return usuario