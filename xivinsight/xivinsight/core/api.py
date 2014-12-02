from rest_framework import viewsets

from . import models, serializers

class AttackTypeViewSet(viewsets.ModelViewSet):
    queryset = models.AttackType.objects.all()
    serializer_class = serializers.AttackTypeSerializer

class CombatantViewSet(viewsets.ModelViewSet):
    queryset = models.Combatant.objects.all()
    serializer_class = serializers.CombatantSerializer

class CurrentViewSet(viewsets.ModelViewSet):
    queryset = models.Current.objects.all()
    serializer_class = serializers.CurrentSerializer

class DamageTypeViewSet(viewsets.ModelViewSet):
    queryset = models.DamageType.objects.all()
    serializer_class = serializers.DamageTypeSerializer

class EncounterViewSet(viewsets.ModelViewSet):
    queryset = models.Encounter.objects.all()
    serializer_class = serializers.EncounterSerializer

class SwingViewSet(viewsets.ModelViewSet):
    queryset = models.Swing.objects.all()
    serializer_class = serializers.SwingSerializer
