from django.urls import path

from .views import ViewCoreUser
from .views import ViewCoreUserUpdate
from .views import ViewCreateCore
from .views import ViewDeleteCore
from .views import (
    ViewDeleteUserCore,
)
from .views import ViewListCore
from .views import ViewUpdateCore

urlpatterns = [
    path('create/', ViewCreateCore.as_view(), name='create_core'),
    path('list/', ViewListCore.as_view(), name='list_core'),
    path('update/<int:pk>/', ViewUpdateCore.as_view(), name='update_core'),
    path('delete/<int:pk>/', ViewDeleteCore.as_view(), name='delete_core'),
    path('delete_user/<int:pk>/', ViewDeleteUserCore.as_view(), name='delete'),
    path(
        'update_user/<int:pk>/',
        ViewCoreUserUpdate.as_view(), name='update_user',
    ),
    path('user/<int:pk>/', ViewCoreUser.as_view(), name='user'),
]
