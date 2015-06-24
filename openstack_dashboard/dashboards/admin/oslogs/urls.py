from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.admin.oslogs.views \
    import IndexView
from openstack_dashboard.dashboards.admin.oslogs import views


urlpatterns = patterns(
    'openstack_dashboard.dashboards.admin.oslogs.views',
    url(r'^(?P<node>[^/]+)/$',
        views.AdminDetailView.as_view(),
        name='detail'),
    url(r'^$', IndexView.as_view(), name='index'),
)
