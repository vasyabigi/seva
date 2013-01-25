from django.contrib.auth.models import User

from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.authentication import BasicAuthentication, Authentication
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.throttle import CacheThrottle, CacheDBThrottle
from tastypie import fields

from profiles.models import Profile
from evaluations.models import SelfEvaluation


class UserListResource(ModelResource):
    full_name = fields.CharField()
    avg_level = fields.DecimalField()
    bio = fields.CharField()
    favorites = fields.ListField()
    evaluations = fields.ListField()
    
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

    def dehydrate_avg_level(self, bundle):
        return bundle.obj.get_profile().get_avg_level()

    def dehydrate_favorites(self, bundle):
        return list(SelfEvaluation.objects.filter(user=bundle.obj, is_favorite=True).\
            select_related('technology').values_list('technology__title', flat=True)
        )

    def dehydrate_evaluations(self, bundle):
        evaluations = SelfEvaluation.objects.filter(user=bundle.obj).\
            select_related('technology')
        mapping = lambda x: {
            'technology': x.technology.title,
            'technology_slug': x.technology.slug,
            'logo': x.technology.logo,
            'level': x.level,
            'created': x.created,
            'updated': x.updated,
            'is_favorite': x.is_favorite
        }
        return map(mapping, evaluations)
