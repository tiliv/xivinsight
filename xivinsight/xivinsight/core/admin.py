from django.contrib import admin

from xivinsight.core.models import AttackType, Combatant, Current, DamageType, Encounter, Swing

class AttackTypeAdmin(admin.ModelAdmin):
    list_display = ['encid', 'attacker', 'victim', 'swingtype', 'type', 'starttime', 'endtime', 'duration', 'damage', 'encdps', 'chardps', 'dps', 'average', 'median', 'minhit', 'maxhit', 'resist', 'hits', 'crithits', 'blocked', 'misses', 'swings', 'tohit', 'averagedelay', 'critperc', 'parry', 'parrypct', 'block', 'blockpct', 'dmgreduced', 'overheal']
    list_filter = ['encid', 'attacker', 'victim', 'misses']


class GenericAdmin(admin.ModelAdmin):
    pass

class EncounterAdmin(admin.ModelAdmin):
    date_hiearchy = 'starttime'
    list_display = ['encid', 'title', 'starttime', 'endtime', 'duration', 'damage', 'encdps', 'zone', 'kills', 'deaths']
    list_filter = ['zone', 'title', 'kills', 'deaths']

admin.site.register(AttackType, AttackTypeAdmin)
admin.site.register(Combatant, GenericAdmin)
admin.site.register(Current, GenericAdmin)
admin.site.register(DamageType, GenericAdmin)
admin.site.register(Encounter, EncounterAdmin)
admin.site.register(Swing, GenericAdmin)
