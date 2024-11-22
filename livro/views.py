from rest_framework import generics, response, status, permissions, views
from operator import itemgetter
from .models import Livro
from .serializers import LivroSerializer

class CadastroLivroPorImagem(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        pass

livro_config = {
    "queryset": Livro.objects.all(),
    "permission_classes": [permissions.IsAuthenticated],
    "serializer_class": LivroSerializer,
    "filterset_fields": ["tombo", "titulo", "autor", "local_editora", "ano_edicao", "data_entrada"],
    "ordering_fields": ["tombo", "titulo", "autor", "local_editora", "ano_edicao", "data_entrada"],
}

class LivroLC(generics.ListCreateAPIView):
    queryset, \
    serializer_class, \
    permission_classes, \
    filterset_fields, \
    ordering_fields = itemgetter("queryset", "serializer_class", "permission_classes", "filterset_fields", "ordering_fields")(livro_config)

    def get_queryset(self):
        return Livro.objects.all()

class LivroRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset, \
    serializer_class, \
    permission_classes, \
    filterset_fields, \
    ordering_fields = itemgetter("queryset", "serializer_class", "permission_classes", "filterset_fields", "ordering_fields")(livro_config)

    def get_object(self):
        try:
            return Livro.objects.get(tombo=self.kwargs["pk"])
        except Livro.DoesNotExist:
            return response.Response(detail="Registro não encontrado", status=status.HTTP_404_NOT_FOUND)
