from django.utils.translation import ugettext_lazy as _

from horizon import tables


class InstancesTable(tables.DataTable):
    hostname = tables.Column("hostname",
                             link="horizon:admin:logs:detail",
                             attrs={'data-type': 'naturalSort'},
                             verbose_name=_("Hostname"))

    class Meta:
        name = "nodes"
        verbose_name = _("Nodes")
