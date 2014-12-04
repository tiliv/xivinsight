from datetime import timedelta
from operator import itemgetter

from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

import numpy
from rest_framework import serializers
from rest_framework.fields import Field

from . import models


class TimedeltaField(Field):
    type_name = 'TimedeltaField'
    # form_field_class = forms.FloatField

    default_error_messages = {
        'invalid': _("'%s' value must be in seconds."),
    }

    def to_representation(self, obj):
        return obj.total_seconds()

    def to_internal_value(self, value):
        if value in validators.EMPTY_VALUES:
            return None

        try:
            return datetime.timedelta(seconds=float(value))
        except (TypeError, ValueError):
            msg = self.error_messages['invalid'] % value
            raise ValidationError(msg)




class AttackTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AttackType

class CombatantSerializer(serializers.ModelSerializer):
    ally = serializers.BooleanField(source='is_ally')

    class Meta:
        model = models.Combatant

class CurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Current

class DamageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DamageType

class SwingListSerializer(serializers.ListSerializer):
    @property
    def data(self):
        # NOTE: Skipping super() here because it'll dumb down the dict to a list of its keys
        if not hasattr(self, '_data'):
            self._data = self.to_representation(self.instance)
        return self._data

    def to_representation(self, data):
        objects = super(SwingListSerializer, self).to_representation(data)

        data = {
            'objects': objects,
        }
        data.update(self.get_statistical_values(objects))
        return data

    def get_statistical_values(self, objects):
        deltas = numpy.array(tuple(map(itemgetter('stime_delta'), objects)))
        # median = numpy.median(deltas)
        # if median == numpy.nan:
        #     median = 0
        median = 0
        return {
            'median_stime_delta': median,
        }

class SwingSerializer(serializers.ModelSerializer):

    # Model methods
    is_ability = serializers.BooleanField()
    is_gcd_ability = serializers.BooleanField()
    is_critical_hit = serializers.BooleanField()
    is_dot_tick = serializers.BooleanField()

    # Computed
    stime_delta = TimedeltaField()

    class Meta:
        model = models.Swing
        list_serializer_class = SwingListSerializer


class EncounterSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Encounter


class EncounterSerializer(serializers.ModelSerializer):
    combatants = CombatantSerializer(source='get_combatants', many=True, read_only=True)
    # swings =

    class Meta:
        model = models.Encounter

