from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # media 파일에 대한 스태틱 서브 기능
    import debug_toolbar
    
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
    
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)