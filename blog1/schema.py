import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Article,Category,Comment
from .graphene_Type import *

class Query(graphene.ObjectType):

    articles = graphene.List(ArticleType)

    def resolve_articles(parent, info, **kwargs):
        articles = Article.objects.all()
        return articles
    
    categorys = graphene.List(CategoryType)

    def resolve_category(parent, info, **kwargs):
        cat = Category.objects.all()
        return cat
    
    comments = graphene.List(CommentType)
    
    def resolve_comments(parent, info, **kwargs):
       cm = Comment.objects.all()
       return cm