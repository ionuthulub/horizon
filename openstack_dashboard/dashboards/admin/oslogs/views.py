import os

from horizon import tables
from horizon.tables import views


class IndexView(views.DataTableView):
    table_class = tables.DataTable
    template_name = 'admin/oslogs/index.html'

    def get_data(self):
        nodes = []
        nodes = {'hostname': n for n in os.listdir('/var/log/oslogs')}
        return nodes


class AdminDetailView(tables.DataTableView):
    table_class = []
    template_name = 'admin/hypervisors/detail.html'
    page_title = ("Hypervisor Servers")

    def get_data(self):
        instances = []
        try:
            id, name = self.kwargs['hypervisor'].split('_', 1)
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
