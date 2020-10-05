from basic import views

from django.urls import path


app_name = 'basic'

urlpatterns = [
    path('hello-world/', views.HelloWorldView.as_view(), name='hello-world'),
]
