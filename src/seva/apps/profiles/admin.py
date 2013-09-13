from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from django.template import Context

from profiles.models import Profile


def send_invitation_email(modeladmin, request, queryset):
    """
        Resets user password to randomly generated and sends email with greetings and credentials
    """
    for user in queryset:
        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.is_staff=True
        group = Group.objects.get(name='Team')
        user.groups.add(group)

        subject, from_email, to = 'You have bean invited to DS Seva!', settings.DEFAULT_FROM_EMAIL, user.email

        context = Context({ 'user': user, 'password': new_password })
        text_content = get_template('profile/invitation_email.txt').render(context)
        html_content = get_template('profile/invitation_email.html').render(context)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        user.save()

send_invitation_email.short_description = 'Reset user\'s password and send invitation with new one.'


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'joined', 'number', 'dont_track_in_avg')
    list_editable = ('joined', 'number', 'dont_track_in_avg')


class UserAdmin(DjangoUserAdmin):
    actions = (send_invitation_email,)

admin.site.unregister(User)

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
