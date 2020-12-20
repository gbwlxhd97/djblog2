from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/', include('blogapp.urls')), # blogapp에 url을 따로 관리함으로, include로 임포트 해주는것
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('accounts/', include('accounts.urls')),
]  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media url등록
