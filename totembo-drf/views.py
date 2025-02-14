from django.shortcuts import render
from django.http import HttpResponse
from totembo.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework import permissions



# Create your views here.

# @api_view(['GET', 'POST'])
# def category_list(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = NewCategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
# @api_view(['GET', 'DELETE', 'PUT'])
# def category_update_or_delete(request, pk):
#     category = Category.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         data = request.data
#         serializer = NewCategorySerializer(category, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'DELETE':
#         if not category:
#             return Response({
#                 'Error': 'Category was not found to delete'
#             }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['GET'])
# def product_list(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductsSerializer(products, many=True)
#         return Response(serializer.data)
#
# @api_view()
# def product_by_category(request, pk):
#     category = Category.objects.get(pk=pk)
#     subcategories = category.subcategories.all()
#     products = Product.objects.filter(category__in=subcategories)
#     serializer = ProductByCategory(products, many=True)
#     return Response(serializer.data)
#
# @api_view(['GET'])
# def reviews_by_user(request, pk):
#     if request.method == 'GET':
#         reviews = Reviews.objects.filter(user_id = pk)
#         serializer = ReviewsSerializer(reviews, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET', 'POST'])
# def product_create_view(request, pk):
#     if request.method == 'GET':
#         product = Product.objects.get(pk=pk)
#         serializer = ProductsSerializer(product)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def product_update_or_delete(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         data = request.data
#         serializer = ProductCreateSerializer(product, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     elif request.method == 'DELETE':
#         if not product:
#             return Response({
#                 'Error': 'Product Not found for delete'
#             }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['GET', 'POST'])
# def get_product_by_pk(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         data = request.data
#         data['user'] = request.user.id
#         data['product'] = product.pk
#
#         serializer = ReviewsCreateSerializers2(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# ============================== Views using API VIEW =======================================

# class CategoryListView(APIView):
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategoriesSerializer(categories, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
# class ProductListView(APIView):
#     def get(self, request):
#         products = Product.objects.all().annotate(
#             reviews_count=models.Count(models.F('comments'))
#         )
#         serializer = ProductListSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
#
# class ProductDetailView(APIView):
#     def get(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         serializer = ProductDetailSerializer2(product)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, pk):
#         data = request.data
#         product = Product.objects.get(pk=pk)
#         data['product'] = product.pk
#         data['user'] = request.user.id
#
#         serializer = ReviewCreateSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         print(serializer.errors)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def delete(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         if product:
#             product.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ProductCreateView(APIView):
#     def post(self, request):
#         serializer = ProductCreateSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class OrderView(APIView):
#     def get(self, request, pk):
#         order = OrderProduct.objects.get(pk=pk)
#         serializer = OrderSerializer(order)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
# class ShippingAddressView(APIView):
#     def get(self, request):
#         address = ShippingAddress.objects.all()
#         serializer = ShippingAddressSerializer(address, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class ProductByCategoryView(APIView):
#     def get(self, request, pk):
#         category = Category.objects.get(pk=pk)
#         subcategories = category.subcategories.all()
#         products = Product.objects.filter(category__in=subcategories).annotate(
#             reviews_count=models.Count(models.F('comments'))
#         )
#         serializer = ProductDetailSerializer2(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# Views using generics classes

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer

class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer2

    def get_queryset(self):
        product = Product.objects.annotate(
            reviews_count=models.Count(models.F('average_rating'))
        ).all()
        return product


# ============ ListCreateApiView ============= Have extra conviniences as a style of the page and posting a request is
# much more clearer
class CommentCreateApiView(ListCreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        product = Product.objects.get(pk=self.kwargs['pk'])
        reviews = Reviews.objects.filter(product=product)
        return reviews

