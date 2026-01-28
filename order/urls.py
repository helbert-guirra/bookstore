"""
Arquivo de rotas do app Order.

Responsável por expor as URLs da API relacionadas a pedidos (Order),
utilizando ViewSets do Django REST Framework.
"""

# Importa funções do Django para definição de rotas
from django.urls import include, path

# Importa o sistema de roteamento automático do DRF
from rest_framework import routers

# Importa os ViewSets do app order
# Aqui está a classe OrderViewSet, que contém as ações da API
from order import viewsets


# Cria uma instância de SimpleRouter
# O SimpleRouter gera automaticamente rotas REST
# como list, create, retrieve, update e delete
router = routers.SimpleRouter()


# Registra o OrderViewSet no router
#
# Parâmetros:
# - r"order": prefixo da URL
#   Exemplo: /order/
#
# - viewsets.OrderViewSet: classe responsável pela lógica da API
#
# - basename="order": nome base das rotas
#   Usado para geração dos nomes:
#   - order-list   → GET / POST
#   - order-detail → GET / PUT / DELETE
#
# Esse basename é essencial para uso do reverse() nos testes
router.register(
    r"order",
    viewsets.OrderViewSet,
    basename="order"
)


# Lista de URLs do app order
#
# O include(router.urls) adiciona automaticamente
# todas as rotas criadas pelo router
#
# Essas rotas geralmente são incluídas em um nível superior,
# por exemplo:
# path("api/v1/", include("order.urls"))
urlpatterns = [
    path("", include(router.urls)),
]
