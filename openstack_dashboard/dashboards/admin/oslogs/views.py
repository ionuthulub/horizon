import os

from horizon import tables
from horizon.tables import views
from horizon.utils import functions as utils


class IndexView(views.DataTableView):
    # A very simple class-based view...
    table_class = tables.DataTable
    template_name = 'admin/oslogs/index.html'

    def get_data(self):
        nodes = []
        nodes = {'hostname': n for n in os.listdir('/var/log/oslogs')}
        return nodes
