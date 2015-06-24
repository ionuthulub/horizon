import os

from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import views as horizon_views
from horizon import tables
from horizon.tables import views

from openstack_dashboard.dashboards.admin.oslogs \
    import tables as oslogs_tables


class IndexView(views.DataTableView):
    table_class = oslogs_tables.NodesTable
    template_name = 'admin/oslogs/index.html'
    page_title = _("Nodes")

    def get_data(self):
        nodes = []

        class Node(object):
            def __init__(self, _id, hostname):
                self.id = _id
                self.hostname = hostname

        try:
            nodes = [Node(i, n) for
                     i, n in enumerate(os.listdir('/var/log/oslogs'))]
        except Exception:
            exceptions.handle(self.request,
                              _('Unable to retrieve nodes list.'))

        return nodes


class NodeView(tables.DataTableView):
    table_class = oslogs_tables.LogsTable
    template_name = 'admin/oslogs/node.html'
    page_title = ("Logs")

    def get_data(self):
        logs = []

        class Log(object):
            def __init__(self, _id, name):
                self.id = _id
                self.name = name

        try:
            node = self.kwargs['node']
            logs = [Log(i, n) for
                    i, n in enumerate(os.listdir('/var/log/oslogs/' + node))]
        except Exception:
            exceptions.handle(self.request,
                              _('Unable to retrieve logs list.'))

        return logs


class LogView(horizon_views.HorizonTemplateView):
    template_name = "project/instances/_detail_log.html"
    page_title = _("View log")

    def get_context_data(self, request):
        node_log = self.kwargs('node_log')
        node, log = node_log.split('_', 1)[0], node_log.split('_', 1)[1]
        log_length = self.kwargs('log_length')
        try:
            with open(os.path.join('/var/log/oslogs/', node, log)) as fin:
                data = fin.read()
        except Exception:
            data = _('Unable to read log "%s".') % os.path.join(
                '/var/log/oslogs/', node, log)
            exceptions.handle(request, ignore=True)
        return {"console_log": data,
                "log_length": log_length}