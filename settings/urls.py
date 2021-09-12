from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url
from custom.api.signin import api_signin

urlpatterns = [
    path('customers/', include('modules.customers.urls')),
    path('orders/', include('modules.orders.urls')),
    path('signin/', api_signin, name='api_signin'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
