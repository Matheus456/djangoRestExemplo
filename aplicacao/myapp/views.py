from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Music, Pessoa
from .serializers import MusicSerializer, PessoaSerializer

# Forma mais "engessada"(isso não quer dizer que seja ruim) que eu tinha falado do tutorial.
class MusicList(generics.ListCreateAPIView):

    queryset = Music.objects.all()
    serializer_class = MusicSerializer

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})

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

@api_view(['GET', 'POST']) #'GET', 'POST' são os métodos que eles irão responder
def hello_world2(request):
    # Verifica se o usuário está usando o método POST(Ou seja, "enviando informação")
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

@api_view(['POST'])
def pessoa(request):
    return Response({"Nome": request.data['nome'], "sobrenome": request.data['sobrenome'], "nick": request.data['nick']})


# AHHH NEM, MAS QUANDO EU MANDO ALGO DIFERENTE DO QUE ELE QUER DÁ UM ERRO :'(
# Relaxem, tem como validar(e não é com vários ifs) e 
# aqui vem algo que é semelhante ao forms, que vocês já estudaram ;)
# Até já usamos lá em cima, é o serializers
@api_view(['POST'])
def pessoa2(request):
    serializer = PessoaSerializer(data = request.data)
    if serializer.is_valid():
        # Para salvar o usuário
        pessoa = PessoaSerializer.create(serializer, request.data)
        return Response({"Nome": request.data['nome'], "sobrenome": request.data['sobrenome'], "nick": request.data['nick']})
    else:
        return Response({
            "message": "Meu caro, não me faça gastar processamento com esses dados! Passe a informação correta!",
            "atributos_esperados": "nome, sobrenome, nick, senha"})


# Ahh, mas isso é muito fácil! Queria saber mesmo é como faz para enviar os dados para o usuário!
# Meu abigo, vamos lá!
@api_view(['GET'])
def pessoa3(request):
    pessoas = Pessoa.objects.all()
    serializer = PessoaSerializer(pessoas, many=True)
    return Response(serializer.data) 
