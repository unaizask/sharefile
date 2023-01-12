from django.urls import path
from . import views

urlpatterns = [
    path('handle/', views.HandleFileUpload.as_view(), name = 'handle'),
    path('', views.homeview.as_view(), name = 'home'),
    # path('download/', views.downloadview.as_view(), name='download')
    path('download/<uid>', views.downloadview, name = 'home'),

]