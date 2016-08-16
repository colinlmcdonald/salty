from django.conf.urls import url
import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^surfers/$', views.surfers),
    url(r'^surfers/(?P<surfer_pk>\d+)/$', views.surfer),
    url(r'^shapers/$', views.shapers),
    url(r'^shapers/(?P<shaper_pk>\d+)/$', views.shaper),
    url(r'^surfboards/$', views.surfboards),
    url(r'^surfboards/(?P<surfboard_pk>\d+)/$', views.surfboard),
    url(r'^surfboard_models/$', views.surfboard_models),
    url(r'^surfboard_models/(?P<surfboard_model_pk>\d+)/$', views.surfboard_model),
]
