from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, plus_product_amount, minus_product_amount, remove_product, edit_product, delete_product, get_product_json, add_product_ajax





app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('plus_product_amount/<int:id>', plus_product_amount, name='plus_product_amount'),
    path('minus_product_amount/<int:id>', minus_product_amount, name='minus_product_amount'),
    path('remove_product/<int:id>', remove_product, name='remove_product'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('delete/<int:id>', delete_product, name='delete_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax')
]