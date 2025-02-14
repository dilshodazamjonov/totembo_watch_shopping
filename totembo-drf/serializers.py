from rest_framework import serializers
from totembo.models import *


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'title', 'slug', 'parent']
#
#
# class NewCategorySerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=250)
#     parent = serializers.PrimaryKeyRelatedField(allow_null=True, label='Категория', queryset=Category.objects.all(), required=False)
#
#     def create(self, validated_data):
#         return Category.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.parent = validated_data.get('parent', instance.parent)
#         instance.slug = validated_data.get('slug', instance.slug)
#         instance.save()
#         return instance
#
#
# class ReviewsSerializer(serializers.ModelSerializer):
#     user = serializers.SlugRelatedField(slug_field='username', read_only=True)
#
#     class Meta:
#         model = Reviews
#         fields = ['text', 'user', 'product', 'created_at']
#
#
# # Creating Reviews with own serializer
#
# class ReviewsCreateSerializer(serializers.Serializer):
#     text = serializers.CharField()
#     user_id = serializers.IntegerField()
#     product_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Reviews.objects.create(**validated_data)
#
#
#
# # Creating reviews using ModelSerializer
#
# class ReviewsCreateSerializers2(serializers.ModelSerializer):
#
#     class Meta:
#         model = Reviews
#         fields = ('text', 'user', 'product')
#
#
#
#
# class ProductsSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     description = serializers.CharField()
#     price = serializers.FloatField()
#     discount = serializers.IntegerField()
#     created_at = serializers.DateTimeField()
#     category = serializers.SlugRelatedField(slug_field='title', read_only=True)
#     model = serializers.SlugRelatedField(slug_field='title', read_only=True)
#     comments = ReviewsSerializer(many=True)
#
# class ProductSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     description = serializers.CharField()
#     price = serializers.FloatField()
#     discount = serializers.IntegerField()
#     created_at = serializers.DateTimeField()
#     category = serializers.SlugRelatedField(slug_field='title', read_only=True)
#     model = serializers.SlugRelatedField(slug_field='title', read_only=True)
#     comments = ReviewsSerializer(many=True)
#
#
#
# class ProductByCategory(serializers.Serializer):
#     title = serializers.CharField()
#     description = serializers.CharField()
#     price = serializers.FloatField()
#     discount = serializers.IntegerField()
#     created_at = serializers.DateTimeField()
#     category = serializers.SlugRelatedField(slug_field='title', read_only=True)
#     model = serializers.SlugRelatedField(slug_field='title', read_only=True)
#     comments = ReviewsSerializer(many=True)
#
#
#
# # Serializer for adding a new product
# class ProductCreateSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     description = serializers.CharField()
#     category_id = serializers.IntegerField()
#     price = serializers.FloatField()
#
#     def create(self, validated_data):
#         product = Product.objects.create(**validated_data)
#         return product
#
#     # method for updating the game
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.category = validated_data.get('category', instance.category)
#         instance.save()
#         return instance
#
#


# Serializations for views in class

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('title',)

class ProductListSerializer(serializers.ModelSerializer):
    reviews_count = serializers.IntegerField()

    class Meta:
        model = Product
        exclude = ('id', 'color', 'color_code', 'updated_at')

class ReviewsSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='title', read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Reviews
        fields = ('text', 'user', 'product')

# class ProductDetailSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     description = serializers.CharField()
#     price = serializers.FloatField()
#     discount = serializers.IntegerField()
#     created_at = serializers.DateTimeField()
#     category = serializers.SlugRelatedField(slug_field='title', read_only=True)
#     model = serializers.SlugRelatedField(slug_field='title', read_only=True)
#     comments = ReviewsSerializer(many=True)

# =========================== Do the above task with the ModelSerializer ========================

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = ('image',)




class ProductDetailSerializer2(serializers.ModelSerializer):
    comments = ReviewsSerializer(many=True, read_only=True)
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    model = serializers.SlugRelatedField(slug_field='title', read_only=True)
    images = ProductImagesSerializer(instance='image', many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'images', 'price', 'discount',
                  'model', 'category', 'comments', 'average_rating']

class ProductCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    category_id = serializers.IntegerField()
    model_id = serializers.IntegerField()
    price = serializers.FloatField()
    discount = serializers.IntegerField()

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        return product


class OrderSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='title', read_only=True)


    class Meta:
        model = OrderProduct
        exclude = ('id', 'updated_at')

class GetCustomerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Customer
        fields = ('user',)


class ShippingAddressSerializer(serializers.ModelSerializer):
    customer = GetCustomerSerializer(instance='user', read_only=True)
    region = serializers.SlugRelatedField(slug_field='title', read_only=True)
    city = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = ShippingAddress
        fields = ('address', 'phone', 'comment', 'created_at', 'customer', 'order', 'region', 'city')


class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = ('text', 'user', 'product')
