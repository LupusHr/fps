from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'fps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path(r'admin/', admin.site.urls),
    path(r'', include('fps_glavni.urls', namespace='url_glavni')),
]
