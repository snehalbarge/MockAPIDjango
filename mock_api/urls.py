from django.contrib import admin
from django.urls import path
from mock_api_app.views import PersonList,index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('person',PersonList.as_view(),name="call"),
]
