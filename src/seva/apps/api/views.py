from django.contrib.auth.models import User
from django.db.models import Avg

from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.authentication import BasicAuthentication, Authentication
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.throttle import CacheThrottle, CacheDBThrottle
from tastypie import fields
from tastypie.cache import SimpleCache

from profiles.models import Profile
from evaluations.models import SelfEvaluation
from technologies.models import Technology


class UserListResource(ModelResource):
    full_name = fields.CharField()
    avg_level = fields.DecimalField()
    bio = fields.CharField()
    favorites = fields.ListField()
    evaluations = fields.ListField(use_in='detail')
    joined = fields.DateField()
    number = fields.CharField()

    class Meta:
        queryset = User.objects.all().select_related('profile')
        allowed_methods = ['get',]
        resource_name = 'users'
        serializer = Serializer(formats=['json',])
        authentication = Authentication()
        authorization = Authorization()
        throttle = CacheDBThrottle(
            throttle_at=50, timeframe=60,
            expiration=24*60*60
        )
        excludes = (
            'password', 'date_joined', 'is_staff', 'is_superuser',
            'first_name', 'last_name'
        )
        detail_uri_name = 'username'

    def dehydrate_joined(self, bundle):
        return bundle.obj.profile.joined

    def dehydrate_number(self, bundle):
        return bundle.obj.profile.number

    def dehydrate_full_name(self, bundle):
        return bundle.obj.get_full_name()

    def dehydrate_bio(self, bundle):
        return bundle.obj.get_profile().bio

    def dehydrate_avg_level(self, bundle):
        return bundle.obj.get_profile().get_avg_level()

    def dehydrate_favorites(self, bundle):
        return list(SelfEvaluation.objects.filter(user=bundle.obj, is_favorite=True).\
            select_related('technology').values('technology__title',  'technology__slug')
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



class TechnologyResource(ModelResource):
    avg = fields.DecimalField()
    evaluations = fields.ListField(blank=True, use_in='detail')

    def dehydrate_avg(self, bundle):
        return  bundle.obj.selfevaluation_set.exclude(user__profile__dont_track_in_avg=True).aggregate(Avg('level'))['level__avg']

    def dehydrate_evaluations(self, bundle):
        sl = SelfEvaluation.objects.filter(technology=bundle.obj)
        return [
            {
                'username': i.user.username,
                'level': i.level,
                'full_name': i.user.get_full_name(),
                'favorite': i.is_favorite
            } for i in sl
        ]

    class Meta:
        queryset = Technology.objects.all().select_related('selfevaluation', 'selfevaluation__user')
        serializers = Serializer(formats=['json', ])
        fields = ('title', 'slug')
        detail_uri_name = 'slug'
        limit = 200
        throttle = CacheDBThrottle(
            throttle_at=50, timeframe=60,
            expiration=24*60*60
        )
        allowed_methods = ['get',]
        # cache = SimpleCache(timeout=30)

