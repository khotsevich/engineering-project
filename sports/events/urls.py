from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('', views.events, name='events'),
		# path('<int:id>/', views.detail, name='detail'),
]