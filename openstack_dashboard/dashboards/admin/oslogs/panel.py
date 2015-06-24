from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.admin import dashboard


class Oslogs(horizon.Panel):
    name = _("Logs")
    slug = "logs"


dashboard.Admin.register(Oslogs)
