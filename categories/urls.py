from django.conf.urls import url
from . import views
from djangoFinal2.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.category_list, name="category_list"),
    url(r'^create/$', views.create_category, name="create_category"),
    url(r'^update/(?P<category_id>[\w-]+)/$', views.update_category),
    url(r'^delete/(?P<category_id>[\w-]+)/$', views.delete_category),
]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)