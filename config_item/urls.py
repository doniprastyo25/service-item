from django.contrib import admin
from django.urls import path
from modernrpc.views import RPCEntryPoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path("rpc/", RPCEntryPoint.as_view())
]
