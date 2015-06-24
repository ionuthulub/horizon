from django.utils.translation import ugettext_lazy as _

from horizon import tables


class NodesTable(tables.DataTable):
    hostname = tables.Column("hostname",
                             link="horizon:admin:logs:detail",
                             verbose_name=_("Hostname"))

    def get_object_id(self, node):
        return "%s_%s" % (node.id, node.hostname)

    class Meta:
        name = "nodes"
        verbose_name = _("Nodes")
