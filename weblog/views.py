from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticatedOrReadOnly

from .models import Article
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


def index_page(request):
    articles = Article.objects.order_by("published_at")[:10]
    articles = articles[::-1]

    context = {
        "articles": articles,
    }
    return render(request, "weblog/index.html", context)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def articles_json(request: Request):
    articles = list(Article.objects.order_by("published_at").all().values_list(
        'title', 'author', 'content', 'published_at', 'is_published'))
    return Response(
        {'articles': articles}, status=status.HTTP_200_OK
    )
