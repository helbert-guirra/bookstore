"""
Arquivo de rotas do app Product.

Responsável por expor as URLs da API relacionadas a produtos (Product)
e categorias (Category), utilizando ViewSets do Django REST Framework.
"""

# Importa funções do Django para definição de rotas
from django.urls import include, path

# Importa o sistema de roteamento automático do DRF
from rest_framework import routers

# Importa os ViewSets do app product
# - ProductViewSet: gerencia operações CRUD de produtos
# - CategoryViewSet: gerencia operações CRUD de categorias
from product import viewsets


# Cria uma instância de SimpleRouter
# O SimpleRouter gera automaticamente as rotas REST padrão:
# - list   (GET)
# - create (POST)
# - retrieve (GET /<id>/)
# - update / partial_update (PUT / PATCH)
# - destroy (DELETE)
router = routers.SimpleRouter()


# Registra o ViewSet de produtos
#
# r"product":
#   Prefixo da URL
#   Exemplo:
#   - GET    /product/
#   - POST   /product/
#   - GET    /product/{id}/
#
# viewsets.ProductViewSet:
#   Classe que contém a lógica da API de produtos
#
# basename="product":
#   Nome base das rotas geradas:
#   - product-list
#   - product-detail
router.register(
    r"product",
    viewsets.ProductViewSet,
    basename="product"
)


# Registra o ViewSet de categorias
#
# r"category":
#   Prefixo da URL
#   Exemplo:
#   - GET    /category/
#   - POST   /category/
#   - GET    /category/{id}/
#
# viewsets.CategoryViewSet:
#   Classe responsável pela API de categorias
#
# basename="category":
#   Nome base das rotas geradas:
#   - category-list
#   - category-detail
router.register(
    r"category",
    viewsets.CategoryViewSet,
    basename="category"
)


# Lista de URLs do app product
#
# include(router.urls) injeta automaticamente
# todas as rotas REST geradas pelo router
#
# Normalmente este arquivo é incluído em um nível superior,
# por exemplo:
#
# path("api/v1/", include("product.urls"))
urlpatterns = [
    path("", include(router.urls)),
]
