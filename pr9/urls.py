"""pr9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from pr9 import views
from summary import views
from api import views
from . import settings
from summary.views import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="functional"),
    path('summary/', include('summary.urls')),
    path('api/<str:s>', views.ReplacerView.as_view(), name="Replacer"),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui",
    ),
    path('img/', views.ImageFromPillowView.as_view(), name="image")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
