from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.base, name='base'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('sales/', views.sales, name='sales'),
    path('signout/', views.signout, name='signout'),
    path(
        'product/list', 
        views.product, 
        name='product'
        ),
    path('purchase/', views.purchase, name='purchase'),
    path('dispatch/<item>', views.dispatch, name='dispatch'),
    path('display_details/<iid>', views.display_details, name='display_details'),
    path(
        'product/<str:action>/<int:pid>', 
        views.manage_product, 
        name='manage_product'
        ),
    path(
        'stock/', 
        views.stock, 
        name='stock'
        ),
    path('stockRoute/<flag>', views.stockRoute, name='stockRoute'),
    path('update_stock/', views.update_stock, name='update_stock'),
    path('sale_search/', views.sale_search, name='sale_search'),
    path('sale_info/', views.sale_info, name='sale_info'),
    path('summeryByDate/', views.summeryByDate, name='summeryByDate'),
    path('buyItem/', views.buyItem, name='buyItem'),
    path('buyRoute/<dataItem>', views.buyRoute, name='buyRoute'),
    path(
        'products/sales/', 
        views.sale_item, 
        name='sale_item'
        ),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('verifyOtp/', views.verifyOtp, name='verifyOtp'),
    path(
        'sale/add/<int:pid>',
        views.add_to_card,
        name="add_to_cart"
    ),
    path(
        'cart-detail/',
        views.cart_detail,
        name='cart_detail'
    ),
    path(
        'cart/remove/<int:item>/',
        views.remove_cart_item,
        name='remove_cart_item'
    ),
    path(
        'cart/quantity/<int:pk>/<str:action>/',
        views.change_quantity,
        name='change_quantity'
    ),
    path(
        'product/search',
        views.search_product,
        name="search-products",
    )
]