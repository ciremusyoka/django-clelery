from django.urls import path


from .views import AnsView

urlpatterns = [
    path('test/', AnsView.as_view(), name='test')
]