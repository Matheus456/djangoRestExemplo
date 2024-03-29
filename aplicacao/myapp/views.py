from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Music, Pessoa
from .serializers import MusicSerializer, PessoaSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Forma mais "engessada"(isso não quer dizer que seja ruim) que eu tinha falado do tutorial(https://medium.com/@marcosrabaioli/criando-uma-api-rest-utilizando-django-rest-framework-parte-1-55ac3e394fa)
# Acesso: http://localhost:8000/musics/
class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

# Utilizando o segundo link que foi passado(https://www.django-rest-framework.org/api-guide/views/#function-based-views)
# Acesso: http://localhost:8000/hello/
@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Oi a!"})

# Quando forem enviar uma requisição vocês terão que usar o formato JSON, 
# é bem simples, basta dar uma olhada na net. Mas segue abaixo alguns exemplos...

# {
#   "teste_parâmetro": "teste_valor"
# }

# {
#   "nome": "João",
#   "sobrenome": "Robesvildo",
#   "senha": "soulindo",
#   "nick": "joaovildo"
# }

# Imprimindo todos os dados que vem do request
# Acesso: http://localhost:8000/hello2/
@api_view(['GET', 'POST']) #'GET', 'POST' são os métodos que eles irão responder
def hello_world2(request):
    # Verifica se o usuário está usando o método POST(Ou seja, "enviando informação")
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

# Imprimindo informaçẽos específicas que são recebidas do request
# Acesso: http://localhost:8000/pessoa1/


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
def pessoa(request):
    print("TESTE")
    print(request.data['username'])
    print(request.data['password'])
    return Response({"username": "O desgraçado é um gênio", "password": request.data['password']})

# Validando resposta e salvando no banco
# Acesso: http://localhost:8000/pessoa2/
@api_view(['POST'])
def pessoa2(request):
    serializer = PessoaSerializer(data = request.data)
    if serializer.is_valid():
        # Para salvar o usuário
        # pessoa = PessoaSerializer.create(serializer, request.data)
        # Não é necessário sobrescrever o método create para criar um usuário, é possível fazer isso com a linha abaixo.
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retornando index de Pessoa
# Acesso: http://localhost:8000/pessoa3/
@api_view(['GET'])
def pessoa3(request):
    pessoas = Pessoa.objects.all()
    serializer = PessoaSerializer(pessoas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def teste(request):
    print(request.data)
    return Response([{"Nome": "Carlos"}, {"Nome": "Joana"}])