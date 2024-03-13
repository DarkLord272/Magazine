from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.urls import path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    url("admin/", admin.site.urls),
    url(('cart/'), include('cart.urls', namespace='cart')),
    url(('orders/'), include('orders.urls', namespace='orders')),
    
    url(_('coupons/'), include('coupons.urls', namespace='coupons')),
    url('rosetta/', include('rosetta.urls')),
	
    url('', include('shop.urls', namespace='shop')),
	
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
