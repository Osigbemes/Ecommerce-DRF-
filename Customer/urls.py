from django.urls import path
from .views import CreateView, UserView

urlpatterns = [
    path('create_user', UserView.as_view(), name="create")
]