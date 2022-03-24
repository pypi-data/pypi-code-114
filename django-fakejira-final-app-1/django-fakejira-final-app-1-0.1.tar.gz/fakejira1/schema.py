import graphene
from .models import Shipping
from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType


class ShippingNode(DjangoObjectType):
    class Meta:
        model = Shipping
        # Allow for some more advanced filtering here
        interfaces = (Node,)
        fields = "__all__"
        filter_fields = {
            "product": ["exact", "icontains", "istartswith"],
            "customer": ["exact", "icontains", "istartswith"],
            "shipping_status": ["exact"],
        }


class Query(graphene.ObjectType):
    shipping = Node.Field(ShippingNode)
    all_shippings = graphene.List(ShippingNode)
    
    def resolve_all_shippings(root, info):
        # We can easily optimize query count in the resolve method
        return Shipping.objects.all()

    def resolve_category_by_product(root, info, pk):
        try:
            return Shipping.objects.get(id=pk)
        except Shipping.DoesNotExist:
            return None



class ShippingInput(graphene.InputObjectType):
    id = graphene.ID()
    product = graphene.String()
    customer = graphene.String()


class CreateShipping(graphene.Mutation):
    class Arguments:
        shipping_data = ShippingInput(required=True)

    shipping = graphene.Field(ShippingNode)

    @staticmethod
    def mutate(root, info, shipping_data=None):
        shipping_instance = Shipping( 
            id=shipping_data.id,
            product=shipping_data.product,
            customer=shipping_data.customer,
        )
        shipping_instance.save()
        return CreateShipping(book=shipping_instance)


class UpdateShipping(graphene.Mutation):
    class Arguments:
        shipping_data = ShippingInput(required=True)

    shipping = graphene.Field(ShippingNode)

    @staticmethod
    def mutate(root, info, shipping_data=None):

        shipping_instance = Shipping.objects.get(pk=shipping_data.id)

        if shipping_instance:
            shipping_instance.id=shipping_data.id,
            shipping_instance.product=shipping_data.product,
            shipping_instance.customer=shipping_data.customer,
            shipping_instance.save()

            return UpdateShipping(shipping=shipping_instance)
        return UpdateShipping(shipping=None)


class DeleteShipping(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    book = graphene.Field(ShippingNode)

    @staticmethod
    def mutate(root, info, id):
        shipping_instance = Shipping.objects.get(pk=id)
        shipping_instance.delete()

        return None


class Mutation(graphene.ObjectType):
    create_shipping = CreateShipping.Field()
    update_shipping = UpdateShipping.Field()
    delete_shipping = DeleteShipping.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)