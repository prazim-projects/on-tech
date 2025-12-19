"""
URL configuration for on_elec_ctf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from .schema import schema
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotAllowed

@csrf_exempt
def graphql_message(request):
    if request.method == "GET":
        return HttpResponse(
            "<h2>Welcome to the OG GraphQL API version endpoint Bud</h2>"
            "<p>You are on the right path??? fuzz some more just for the fun of it</p>",
            content_type="text/html",
            status=405
        )
    if request.method == "POST":
        view = csrf_exempt(GraphQLView.as_view(graphiql=False, schema=schema))

    return view(request)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('ctf/', include('ctf.urls')),
    path('api/', include('api.urls')),
    path('v2/api/graphql/', csrf_exempt(GraphQLView.as_view(graphiql=False, schema=schema))),
    path('accounts/', include('django.contrib.auth.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)