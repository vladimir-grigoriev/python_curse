from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('s-admin/', admin.site.urls),
    path('admin/', include('manager_admin.urls', namespace='manager_admin')),
    path('', include('hello_world.urls', namespace='hello_world')),
    path('directories/', include('directory.urls'), name='hello'),
    path('products/', include('products.urls', namespace='products')),
    path('registration/', include('registration.urls', namespace='registration')),
    path('login/', include('login.urls', namespace='login')),
    path('cart/', include('orders.urls', namespace='orders')),
    path('profile/', include('user_profile.urls', namespace='user_profile')),
    path('comments/', include('comments.urls', namespace='comments'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)