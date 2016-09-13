from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import renderers
from rest_framework import response
from rest_framework import schemas
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from core.views import StudentViewSet, UniversityViewSet


@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer, renderers.CoreJSONRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Student Directory API')
    return response.Response(generator.get_schema(request=request))


router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^api/v1/docs/$', schema_view),
    url(r'^api/v1/', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
