
from django.contrib import admin
from django.urls import path , include
import blog.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/', include('blog.urls')), # blog폴더에 urls파일의 정보를 include 해라. 시작 url은 blog/
                                         # 사용하려면 include를 import 받아야함.
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 병렬적으로 추가 (좀더 효율적, 추후에 학습 필요) (urlpatterns += (~~)와 같음)
