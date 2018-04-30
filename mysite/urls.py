from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    # url(r'^polls/', include('polls.urls', namespace="polls")),
]
