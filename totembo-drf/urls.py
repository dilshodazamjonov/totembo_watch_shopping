from django.urls import path
from .views import *


urlpatterns = [
    # path('api/v1/categories/', category_list),
    # path('api/v1/category_delete_update/<int:pk>/', category_update_or_delete),
    # path('api/v1/products/', product_list),
    # path('api/v1/product/<int:pk>/', get_product_by_pk),
    # path('api/v1/products_by_category/<int:pk>/', product_by_category),
    # path('api/v1/product_create/<int:pk>/', product_create_view),
    # path('api/v1/product_delete_update/<int:pk>/', product_update_or_delete),
    # path('api/v1/review_by_user/<int:pk>/', reviews_by_user),

    # ====================== URLs for Views written in Classes =====================

    path('api/v1/categories/', CategoryListView.as_view()),
    # path('api/v1/products/', ProductListView.as_view()),
    path('api/v1/product/<int:pk>/', ProductDetailView.as_view()),
    path('api/v1/comments/<int:pk>/', CommentCreateApiView.as_view())
    # path('api/v1/order/<int:pk>/', OrderView.as_view()),
    # path('api/v1/shipping_addresses/', ShippingAddressView.as_view()),
    # path('api/v1/product_create/', ProductCreateView.as_view()),
    # path('api/v1/product_by_category/<int:pk>/', ProductByCategoryView.as_view())
]