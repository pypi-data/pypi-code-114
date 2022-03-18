from rest_framework import generics, views, status, permissions
from rest_framework.response import Response

from commerce.models.product import Product
from commerce.serializers.product_serializer import ProductSerializer, GenericProductSerializer
from commerce.utils.response import prepare_create_success_response, prepare_success_response, prepare_error_response


class AllProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = GenericProductSerializer


class CreateListProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(owner=self.request.user)
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            else:
                return Response(prepare_error_response('You have no permission to add product'),
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(prepare_success_response(str(e)), status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        product = Product.objects.filter(owner=self.request.user)
        if product:
            serializer = ProductSerializer(product, many=True)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        else:
            return Response(prepare_error_response('No Product found'), status=status.HTTP_400_BAD_REQUEST)


class ProductDetailsUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    def update(self, request, *args, **kwargs):
        _slug = self.request.data.get('slug')
        serializer = ProductSerializer(Product.objects.get(slug=_slug), data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(owner=request.user)
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteAPIView(views.APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return None

    def delete(self, request, pk):
        instance = self.get_object(pk)
        if instance:
            instance.delete()
            return Response(prepare_success_response('Data deleted successfully'), status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(prepare_error_response('Content Not found'), status=status.HTTP_400_BAD_REQUEST)
