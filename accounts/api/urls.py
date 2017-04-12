from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^new$', views.CreateAccountAPIView.as_view(), name="new"),
	url(r'^list$', views.ListAccountAPIView.as_view(), name="list"),
]