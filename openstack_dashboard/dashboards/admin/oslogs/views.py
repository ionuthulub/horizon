import os

from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon.tables import views
from horizon import tables

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
            node = self.kwargs['node'].split('_', 1)
            logs = [Log(i, n) for
                    i, n in enumerate(os.listdir('/var/log/oslogs/' + node))]
        except Exception:
            exceptions.handle(self.request,
                              _('Unable to retrieve logs list.'))

        return logs