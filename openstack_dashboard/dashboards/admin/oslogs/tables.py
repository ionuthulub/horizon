from django.utils.translation import ugettext_lazy as _

from horizon import tables


class NodesTable(tables.DataTable):
    hostname = tables.Column("hostname",
                             link="horizon:admin:oslogs:node",
                             verbose_name=_("Hostname"))

    def get_object_id(self, node):
        return "%s_%s" % (node.id, node.hostname)

    class Meta:
        name = "nodes"
        verbose_name = _("Nodes")


class LogsTable(tables.DataTable):
    name = tables.Column("name",
                         link="horizon:admin:oslogs:log",
                         verbose_name=_("Name"))

    def get_object_id(self, log):
        return "%s_%s" % (log.id, log.name)

    class Meta:
        name = "logs"
        verbose_name = _("Logs")
