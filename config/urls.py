
from django.contrib import admin
from django.urls import include, path
from blog.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', HomePageView.as_view(), name='home')
]