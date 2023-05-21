from django.contrib import admin
from django.urls import path, include
from company_api.views import home_page
from api.views import CompanyViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)


urlpatterns = [
    path('',include(router.urls))
]
