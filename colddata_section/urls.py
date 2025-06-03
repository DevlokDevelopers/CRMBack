from django.urls import path
from .views import receive_cold_data
urlpatterns = [
    path('cold_data_collection/',receive_cold_data,name="cold_data")

]