from django.urls import path, re_path
from account.views import AccountListCreateView
from .views import *

urlpatterns = [
    path('account/', AccountListCreateView.as_view()),

    path('account_type/', AccountTypeListCreateView.as_view()),
    re_path('account_type/(?P<pk>[0-9a-f-]+)', AccountTypeRetrieveUpdateDestroyView.as_view()),
]
