import os

from django.utils.translation import ugettext_lazy as _
from django.shortcuts import HttpResponse
from django.conf import settings

from horizon import exceptions
from horizon import views as horizon_views
from horizon import tables
from horizon.tables import views

from openstack_dashboard.dashboards.admin.oslogs \
    import tables as oslogs_tables


try:
    OSLOGS_PATH = settings.OSLOGS_PATH
except AttributeError:
    OSLOGS_PATH = '/var/log/oslogs/'


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
                     i, n in enumerate(os.listdir(OSLOGS_PATH))]
        except Exception:
            exceptions.handle(self.request,
                              _('Unable to retrieve nodes list.'))

        return nodes


class NodeView(tables.DataTableView):
    table_class = oslogs_tables.LogsTable
    template_name = 'admin/oslogs/node.html'
    page_title = _("{{ node }} logs")

    def get_data(self):
        logs = []

        class Log(object):
            def __init__(self, _id, name):
                self.id = _id
                self.name = name
                self.path = ""

        try:
            node = self.kwargs['node']
            logs = [Log(i, n) for
                    i, n in enumerate(os.listdir(OSLOGS_PATH + node))
                    if not n.endswith('.path')]
            for log in logs:
                try:
                    path = open(
                        os.path.join(OSLOGS_PATH, node, log.name + '.path'),
                        'r').read().strip()
                    log.path = path
                except Exception:
                    pass
        except Exception:
            exceptions.handle(self.request,
                              _('Unable to retrieve logs list.'))

        return logs

    def get_context_data(self, **kwargs):
        context = super(NodeView, self).get_context_data(**kwargs)
        context['node'] = self.kwargs['node']
        return context


class LogView(horizon_views.HorizonTemplateView):
    template_name = "admin/oslogs/log.html"
    page_title = _("{{ node }}")

    def get_context_data(self, *args, **kwargs):
        node_log = self.kwargs['node_log']
        node, log = node_log.split('_', 1)[0], node_log.split('_', 1)[1]
        try:
            with open(os.path.join(OSLOGS_PATH, node, log)) as fin:
                data = ''.join(fin.readlines()[-35:])
        except Exception:
            data = _('Unable to read log "%s".') % os.path.join(
                OSLOGS_PATH, node, log)
        return {"console_log": data,
                "log_length": 35,
                "node": node,
                "log": log}


def bare_log(request, node_log):
    node, log = node_log.split('_', 1)[0], node_log.split('_', 1)[1]
    tail = int(request.GET.get('length', 0))
    try:
        with open(os.path.join(OSLOGS_PATH, node, log)) as fin:
            data = fin.readlines()[-tail:]
    except Exception:
        data = _('Unable to read log "%s".') % os.path.join(
            OSLOGS_PATH, node, log)
    return HttpResponse(data, content_type="text/plain")