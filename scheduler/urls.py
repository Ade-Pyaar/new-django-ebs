
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]


# sauce code: 168479




# just trying to see hoe branching works