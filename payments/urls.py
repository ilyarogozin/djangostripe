from django.urls import path

from .views import (FailView, SuccessView, create_session,
                    item_detail, stripe_config)

urlpatterns = [
    path('config/', stripe_config),
    path('item/<int:id>/', item_detail, name='item'),
    path('buy/<int:id>/', create_session, name='session'),
    path('success/', SuccessView.as_view(), name='success'),
    path('fail/', FailView.as_view(), name='fail'),
]
