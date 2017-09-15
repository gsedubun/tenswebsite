
from django.conf.urls import url,include
from . import views
from .models import Post
from rest_framework import routers, serializers, viewsets

# Serializers define the api representation
class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('author','title')

# viewset to define view behavior.
class  PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Router provider an easy way of automatically determining 
router = routers.DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    url(r'^$', views.index),
    url(r'^post/', include('rest_framework.urls', namespace = 'rest_framework'))
]
