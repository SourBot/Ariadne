from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('A_Blog.urls', namespace="A_Blog_App")),
    path('', include('Ariadne_App.urls')),
]
