from django.db import models

from . import utils

class SwingQuerySet(models.QuerySet):
    def analyze_fields(self):
        return utils.annotate_timestamp_deltas(self, timestamp_field='stime')

    def gcd(self):
        # FIXME: can't tell difference betwen instant/gcd yet
        return self.filter(swingtype=utils.SWING_TYPES['SKILL'])
