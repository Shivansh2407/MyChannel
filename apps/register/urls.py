from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/index.html$', views.index),
    url(r'^Regconf$', views.regconf),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^Main$', views.main),
    url(r'^Main.html$', views.main),
    url(r'^contact.html$', views.contact),
    url(r'^review.html$', views.review),
    url(r'^about.html$', views.about),
    url(r'^Logout.html$', views.logout),
    url(r'^single.html$', views.moviedesc),

]
