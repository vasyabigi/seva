from django.contrib import admin
from django.contrib.auth.models import User
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

        subject, from_email, to = 'You have bean invited to DS Seve!', settings.DEFAULT_FROM_EMAIL, user.email

        plaintext = get_template('profile/invitation_email.txt')
        htmly = get_template('profile/invitation_email.html')
        context = Context({ 'user': user, 'password': new_password })
        text_content = plaintext.render(context)
        html_content = htmly.render(context)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

send_invitation_email.short_description = 'Reset user\'s password and send invitation with new one.'


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'joined', 'number' )
    list_editable = ('joined', 'number')


class UserAdmin(DjangoUserAdmin):
    actions = (send_invitation_email,)

admin.site.unregister(User)

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
