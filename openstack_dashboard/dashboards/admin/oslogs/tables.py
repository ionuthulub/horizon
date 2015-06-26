from django.utils.translation import ugettext_lazy as _

from horizon import tables


class NodesTable(tables.DataTable):
    hostname = tables.Column("hostname",
                             link="horizon:admin:oslogs:node",
                             verbose_name=_("Hostname"))

    def get_object_id(self, node):
        return node.hostname

    class Meta:
        name = "nodes"
        verbose_name = _("Nodes")


class LogsTable(tables.DataTable):
    name = tables.Column("name",
                         link="horizon:admin:oslogs:log",
                         verbose_name=_("Name"))
    path = tables.Column("path",
                         verbose_name=_("Path"))

    def get_object_id(self, log):
        node = self.get_full_url().split('/')[-2]
        return node + '_' + log.name

    class Meta:
        name = "logs"
        verbose_name = _("Logs")
