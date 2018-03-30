from django.conf.urls import url
from django.contrib import admin


from School import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.admin, name='admin login'),
    url(r'^admin_content$', views.admin_content, name='admin_content'),
    url(r'^About$', views.about, name='About'),

    url(r'^teacher_login$', views.teachers, name='Teacher login'),
    url(r'^parents_login$', views.parents, name='Parents login'),

    url(r'^test', views.store, name='store'),
    url(r'^register', views.registration, name='register'),
    url(r'^logintest', views.signup, name='signup')

]
