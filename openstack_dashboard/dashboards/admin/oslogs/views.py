import os

from horizon.tables import views

from openstack_dashboard.dashboards.admin.oslogs import tables


class IndexView(views.DataTableView):
    table_class = tables.NodesTable
    template_name = 'admin/oslogs/index.html'

    def get_data(self):
        class Node(object):
            def __init__(self, _id, hostname):
                self.id = _id
                self.hostname = hostname

        nodes = [Node(i, n) for
                 i, n in enumerate(os.listdir('/var/log/oslogs'))]

        return nodes


class AdminDetailView(object):
    table_class = []
    template_name = 'admin/hypervisors/detail.html'
    page_title = ("Hypervisor Servers")

    def get_data(self):
        instances = []
        try:
            id, name = None, None
            result = None
            for hypervisor in result:
                if str(hypervisor.id) == id:
                    try:
                        instances += hypervisor.servers
                    except AttributeError:
                        pass
        except Exception:
            pass
        return instances
