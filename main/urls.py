from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('summary/', views.summary, name='summary'),
    path('download_summary/', views.download_summary, name='download_summary'),
    path('my_project/', views.my_project, name='my_project'),
    path('download_my_project/', views.download_my_project, name='download_my_project'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
