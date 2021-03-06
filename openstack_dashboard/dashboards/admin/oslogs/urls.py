from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.admin.oslogs.views \
    import IndexView
from openstack_dashboard.dashboards.admin.oslogs import views


urlpatterns = patterns(
    'openstack_dashboard.dashboards.admin.oslogs.views',
    url(r'^(?P<node>[^/_]+)/$',
        views.NodeView.as_view(),
        name='node'),
    url(r'^(?P<node_log>[^/]+)/$',
        views.LogView.as_view(),
        name='log'),
    url(r'^(?P<node_log>[^/]+)/bare/$',
        views.bare_log,
        name='bare_log'),
    url(r'^$', IndexView.as_view(), name='index'),
)
