from django.urls import path
from django.conf.urls import url
from .views import GcodeListAPIView, GcodeCreateAPIView

urlpatterns = [
    path('', GcodeListAPIView.as_view()),
    url(r'upload/(?P<filename>[^/]+)', GcodeCreateAPIView.as_view()),
]
