from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.authentication import BasicAuthentication, Authentication
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.throttle import CacheThrottle, CacheDBThrottle
from tastypie import fields

from profiles.models import Profile
from django.contrib.auth.models import User


class UserListResource(ModelResource):
    full_name = fields.CharField()
    bio = fields.CharField()
    
    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['get',]
        resource_name = 'users'
        serializer = Serializer(formats=['json',])
        authentication = Authentication()
        authorization = Authorization()
        throttle = CacheDBThrottle(
            throttle_at=5, timeframe=60,
            expiration=24*60*60
        )
        always_return_data = True
        excludes = (
            'password', 'date_joined', 'is_staff', 'is_superuser',
            'first_name', 'last_name'
        )
        detail_uri_name = 'username'

    def dehydrate_full_name(self, bundle):
        return bundle.obj.get_full_name()
    
    def dehydrate_bio(self, bundle):
        return bundle.obj.get_profile().bio

class UserResource(ModelResource):
    pass
