from django.conf.urls import url, include
# from . import views
from .api import urls as APIUrls

urlpatterns = [
	url(r'^api/', include(APIUrls, namespace="api")),
]