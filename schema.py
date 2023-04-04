import graphene
import blog1.schema

class Query(blog1.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
