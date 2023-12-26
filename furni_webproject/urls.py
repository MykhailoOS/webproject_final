
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from furni_webproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('furni.urls')),
    path('about/', include('furni.urls', namespace='about')),
    path('shop/', include('furni.urls', namespace='shop')),
    path('services/', include('furni.urls', namespace='services')),
    path('contact/', include('furni.urls', namespace='contact')),
    path('cart/', include('furni.urls', namespace='cart'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
