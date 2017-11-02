"""opticas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include, static
from django.contrib import admin
from django.urls import reverse, reverse_lazy
from django.views.generic import RedirectView
from django.views.static import serve

urlpatterns = [
    url(r'^login/', admin.site.urls),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^', include('services.urls', 'services')),
    url(r'^', include('accounts.urls', 'accounts')),
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('admin:index'))),
]
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
admin.site.site_header = "Sedes Panel"
admin.site.site_title = "Sedes"
