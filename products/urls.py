from django.conf.urls import url
from . import views
from djangoFinal2.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    
    url(r'^$', views.product_index, name="product_index"),
    url(r'^create/$', views.create_product, name="create_product"),
    url(r'^update/(?P<product_id>[\w-]+)/$', views.update_product),
    url(r'^delete/(?P<product_id>[\w-]+)/$', views.delete_product),
]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
    