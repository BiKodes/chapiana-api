from django.urls import path

from .views import GoogleSocialAuthView,FacebookSocialAuthView

app_name='social_auth'

urlpatterns = [
    path('google/', GoogleSocialAuthView.as_view()),
    path('facebook/', FacebookSocialAuthView.as_view()),

]