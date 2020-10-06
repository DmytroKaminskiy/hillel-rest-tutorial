from basic import views

from django.urls import path


app_name = 'basic'

urlpatterns = [
    path('hello-world/', views.HelloWorldView.as_view(), name='hello-world'),
    path('status/', views.StatusCodesView.as_view(), name='statuses'),
    path('status/<int:status_code>', views.StatusCodeInfoView.as_view(), name='status-info'),
]
