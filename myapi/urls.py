
from rest_framework.authtoken.views import obtain_auth_token  
from myapi.crudapp import views as myapp_views
from django.urls import include, path
from rest_framework import routers
from myapi.core import views
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'friends', myapp_views.FriendViewset)
router.register(r'belongings', myapp_views.BelongingViewset)
router.register(r'borrowings', myapp_views.BorrowedViewset)

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  
    path('api/crudops/', include(router.urls)),
]