import graphene
from graphene_django import DjangoObjectType
from products.models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"


class ProductInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String()
    price = graphene.Decimal(required=True)


class UpdateProduct(graphene.Mutation):
    class Arguments:
        input = ProductInput(required=True)
        id = graphene.ID()

    product = graphene.Field(ProductType)

    @classmethod
    def mutate(cls, root, info, input, id):
        product = Product.objects.get(pk=id)
        product.name = input.name
        product.description = input.description
        product.price = input.price
        product.save()
        return UpdateProduct(product=product)


class CreateProduct(graphene.Mutation):
    class Arguments:
        input = ProductInput(required=True)

    product = graphene.Field(ProductType)

    @classmethod
    def mutate(cls, root, info, input):
        product = Product()
        product.name = input.name
        product.description = input.description
        product.price = input.price
        product.save()
        return CreateProduct(product=product)


class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()


class Query(graphene.ObjectType):
    products = graphene.List(ProductType)
    product_by_name = graphene.Field(ProductType, name=graphene.String(required=True))

    def resolve_products(root, info):
        return Product.objects.all()

    def resolve_product_by_name(root, info, name):
        try:
            return Product.objects.get(name=name)
        except Product.DoesNotExist:
            return None


schema = graphene.Schema(query=Query, mutation=Mutation)
