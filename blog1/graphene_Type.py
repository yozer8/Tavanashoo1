import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Article, Category, Comment


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
