from rest_framework import generics, views, status, permissions
from rest_framework.response import Response

from commerce.models.order import Order, OrderItem
from commerce.serializers.order_serializer import OrderSerializer, OrderItemSerializer, OrderListDetailSerializer
from commerce.utils.response import prepare_create_success_response, prepare_success_response, prepare_error_response


class CreateListOrderItemView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.filter(ordered=False)
    serializer_class = OrderItemSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = OrderItemSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=self.request.user)
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(prepare_success_response(str(e)), status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            order_item = OrderItem.objects.filter(user=self.request.user)
            serializer = OrderItemSerializer(order_item, many=True)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        else:
            order_item = OrderItem.objects.all()
            serializer = OrderItemSerializer(order_item, many=True)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)


class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(customer=request.user)
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(prepare_success_response(str(e)), status=status.HTTP_400_BAD_REQUEST)


class OrderListHistoryAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListDetailSerializer

    def list(self, request, *args, **kwargs):
        try:
            if self.request.user.is_superuser:
                order = Order.objects.all().order_by('id')
                serializer = OrderListDetailSerializer(order, many=True)
                return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
            else:
                order = Order.objects.filter(customer=self.request.user, ordered=True).order_by('-id')
                serializer = OrderListDetailSerializer(order, many=True)
                return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(prepare_success_response(str(e)), status=status.HTTP_400_BAD_REQUEST)


class OrderUpdateDetailsView(views.APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get_object(self, order_ide):
        try:
            return Order.objects.get(order_ide=order_ide)
        except Order.DoesNotExist:
            return None

    def get(self, request, order_ide):
        try:
            details = self.get_object(order_ide)
            serializer = OrderListDetailSerializer(details)
            print(serializer.data)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(prepare_success_response(str(e)), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, order_ide):
        try:
            order = self.get_object(order_ide)
            serializer = OrderSerializer(order, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(customer=request.user)
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(prepare_success_response(str(e)), status=status.HTTP_400_BAD_REQUEST)
