from django.urls import path

from commerce.views import category_view
from commerce.views import product_view
from commerce.views import order_view

urlpatterns = [
    # Model API endpoints
    path('model/', category_view.ModelAPIView.as_view(), name='model_api_view'),
    path('model/<pk>/', category_view.ModelUpdateDeleteView.as_view(), name='model_update_delete'),
    # Category API endpoints
    path('category/', category_view.CategoryCrateListView.as_view(), name='category_crate_list'),
    path('category/<pk>/', category_view.CategoryUpdateDeleteView.as_view(), name='category_update_delete'),
    # Brand API endpoints
    path('brand/', category_view.BrandCrateListAPIView.as_view(), name='brand_crate_list'),
    path('brand/<pk>/', category_view.BrandUpdateDeleteView.as_view(), name='brand_update_delete'),
    # product API endpoints
    path('products/', product_view.AllProductsView.as_view(), name='all_products'),
    path('product/', product_view.CreateListProductView.as_view(), name='product_crate_list'),
    path('product/<slug>/', product_view.ProductDetailsUpdateView.as_view(), name='product_update_details'),
    path('product-delete/<pk>/', product_view.ProductDeleteAPIView.as_view(), name='product_delete'),
    # Order Item API endpoints
    path('order-item/', order_view.CreateListOrderItemView.as_view(), name='order_item_list_create'),
    # Order API endpoints
    path('order/', order_view.CreateOrderView.as_view(), name='order_create'),
    path('orders/', order_view.OrderListHistoryAPIView.as_view(), name='order_list_history'),
    path('order/<str:order_ide>/', order_view.OrderUpdateDetailsView.as_view(), name='order_update_details'),
]
