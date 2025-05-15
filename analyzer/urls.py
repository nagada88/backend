from django.urls import path
from .views import UploadMeasurementView

urlpatterns = [
    path('upload/', UploadMeasurementView.as_view(), name='upload_measurement'),
]
