# cookbook/schema.py
import graphene
from graphene_django import DjangoObjectType

from TutTutBolide.polls.models import Voiture, Range, Connector

class RangeType(DjangoObjectType):
    class Meta:
        model = Range
        fields = ("id", "best", "worst", "voiture")

class ConnectorType(DjangoObjectType):
    class Meta:
        model = Range
        fields = ("id", "name", "time", "voiture")
        
class VoitureType(DjangoObjectType):
    class Meta:
        model = Voiture
        fields = ("id", "idBDD", "make", "model", "version", "range", "connectors")

class Query(graphene.ObjectType):
    all_vehicules = graphene.List(VoitureType)
    # category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
    
    def resolve_all_vehicules(root, info):
        # We can easily optimize query count in the resolve method
        return Voiture.objects.select_related("range", "connectors").all()

    # def resolve_category_by_name(root, info, name):
    #     try:
    #         return Category.objects.get(name=name)
    #     except Category.DoesNotExist:
    #         return None

schema = graphene.Schema(query=Query)