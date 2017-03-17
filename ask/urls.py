from django.conf.urls import url, include

from . import views

app_name = 'ask'
urlpatterns = [
    url(r'^$', views.post_question, name='index'),
    url(r'answer/$', views.choose_question),
    url(r'compose/$', views.compose_answer),
    url(r'^charts/bar/$', views.barchart),
]


