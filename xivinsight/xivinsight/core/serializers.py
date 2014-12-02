from rest_framework import serializers

from . import models

class AttackTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AttackType

class CombatantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Combatant

class CurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Current

class DamageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DamageType

class EncounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Encounter

class SwingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Swing
