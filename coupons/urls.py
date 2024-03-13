from django.urls import re_path as url
from . import views

app_name = 'coupons'

urlpatterns = [
	url('apply/$', views.coupon_apply, name='apply'),
]