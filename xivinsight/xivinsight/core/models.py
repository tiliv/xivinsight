from django.db import models

class AttackType(models.Model):
    class Meta:
        managed = False
        db_table = 'attacktype_table'

    encid = models.CharField("ID", max_length=8, primary_key=True)
    attacker = models.CharField("Attacker", max_length=6, null=True, blank=True)
    victim = models.CharField("Victim", max_length=6, null=True, blank=True)
    swingtype = models.IntegerField("Swing type", null=True, blank=True)
    type = models.CharField("Type", max_length=6, null=True, blank=True)
    starttime = models.DateTimeField("Start time")
    endtime = models.DateTimeField("End time", null=True, blank=True)
    duration = models.IntegerField("Duration", null=True, blank=True)
    damage = models.IntegerField("Damage", null=True, blank=True)
    encdps = models.FloatField("EncDPS", null=True, blank=True)
    chardps = models.FloatField("CharDPS", null=True, blank=True)
    dps = models.FloatField("DPS", null=True, blank=True)
    average = models.FloatField("DPS Average", null=True, blank=True)
    median = models.IntegerField("DPS Median", null=True, blank=True)
    minhit = models.IntegerField("Minimum hit", null=True, blank=True)
    maxhit = models.IntegerField("Maximum hit", null=True, blank=True)
    resist = models.CharField("Resist", max_length=6, null=True, blank=True)
    hits = models.IntegerField("Hits", null=True, blank=True)
    crithits = models.IntegerField("Critical hits", null=True, blank=True)
    blocked = models.IntegerField("Blocked", null=True, blank=True)
    misses = models.IntegerField("Misses", null=True, blank=True)
    swings = models.IntegerField("Swings", null=True, blank=True)
    tohit = models.FloatField("To hit", null=True, blank=True)
    averagedelay = models.FloatField("Average delay", null=True, blank=True)
    critperc = models.CharField("Critical %", max_length=8, null=True, blank=True)
    parry = models.IntegerField("Parry", null=True, blank=True)
    parrypct = models.CharField("Parry %", max_length=8, null=True, blank=True)
    block = models.IntegerField("Block", null=True, blank=True)
    blockpct = models.CharField("Block %", max_length=8, null=True, blank=True)
    dmgreduced = models.IntegerField("Damaged reduced", null=True, blank=True)
    overheal = models.IntegerField("Overheal", null=True, blank=True)

    def __str__(self):
        return "{type}".format(**self.__dict__)


class Combatant(models.Model):
    class Meta:
        managed = False
        db_table = 'combatant_table'

    encid = models.CharField(max_length=8, primary_key=True)
    ally = models.CharField(max_length=1, null=True, blank=True)
    name = models.CharField(max_length=64, null=True, blank=True)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    damage = models.IntegerField(null=True, blank=True)
    damageperc = models.CharField(max_length=4, null=True, blank=True)
    kills = models.IntegerField(null=True, blank=True)
    healed = models.IntegerField(null=True, blank=True)
    healedperc = models.CharField(max_length=4, null=True, blank=True)
    critheals = models.IntegerField(null=True, blank=True)
    heals = models.IntegerField(null=True, blank=True)
    curedispels = models.IntegerField(null=True, blank=True)
    powerdrain = models.IntegerField(null=True, blank=True)
    powerreplenish = models.IntegerField(null=True, blank=True)
    dps = models.FloatField(null=True, blank=True)
    encdps = models.FloatField(null=True, blank=True)
    enchps = models.FloatField(null=True, blank=True)
    hits = models.IntegerField(null=True, blank=True)
    crithits = models.IntegerField(null=True, blank=True)
    blocked = models.IntegerField(null=True, blank=True)
    misses = models.IntegerField(null=True, blank=True)
    swings = models.IntegerField(null=True, blank=True)
    healstaken = models.IntegerField(null=True, blank=True)
    damagetaken = models.IntegerField(null=True, blank=True)
    deaths = models.IntegerField(null=True, blank=True)
    tohit = models.FloatField(null=True, blank=True)
    critdamperc = models.CharField(max_length=8, null=True, blank=True)
    crithealperc = models.CharField(max_length=8, null=True, blank=True)
    threatstr = models.CharField(max_length=32, null=True, blank=True)
    threatdelta = models.IntegerField(null=True, blank=True)
    job = models.CharField(max_length=8, null=True, blank=True)
    parrypct = models.CharField(max_length=8, null=True, blank=True)
    blockpct = models.CharField(max_length=8, null=True, blank=True)
    inctohit = models.CharField(max_length=8, null=True, blank=True)
    overhealpct = models.CharField(max_length=8, null=True, blank=True)


class Current(models.Model):
    class Meta:
        managed = False
        db_table = 'current_table'

    encid = models.CharField(max_length=8, primary_key=True)
    ally = models.CharField(max_length=1, null=True, blank=True)
    name = models.CharField(max_length=64, null=True, blank=True)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    damage = models.IntegerField(null=True, blank=True)
    damageperc = models.CharField(max_length=4, null=True, blank=True)
    kills = models.IntegerField(null=True, blank=True)
    healed = models.IntegerField(null=True, blank=True)
    healedperc = models.CharField(max_length=4, null=True, blank=True)
    critheals = models.IntegerField(null=True, blank=True)
    heals = models.IntegerField(null=True, blank=True)
    curedispels = models.IntegerField(null=True, blank=True)
    powerdrain = models.IntegerField(null=True, blank=True)
    powerreplenish = models.IntegerField(null=True, blank=True)
    dps = models.FloatField(null=True, blank=True)
    encdps = models.FloatField(null=True, blank=True)
    enchps = models.FloatField(null=True, blank=True)
    hits = models.IntegerField(null=True, blank=True)
    crithits = models.IntegerField(null=True, blank=True)
    blocked = models.IntegerField(null=True, blank=True)
    misses = models.IntegerField(null=True, blank=True)
    swings = models.IntegerField(null=True, blank=True)
    healstaken = models.IntegerField(null=True, blank=True)
    damagetaken = models.IntegerField(null=True, blank=True)
    deaths = models.IntegerField(null=True, blank=True)
    tohit = models.FloatField(null=True, blank=True)
    critdamperc = models.CharField(max_length=8, null=True, blank=True)
    crithealperc = models.CharField(max_length=8, null=True, blank=True)
    threatstr = models.CharField(max_length=32, null=True, blank=True)
    threatdelta = models.IntegerField(null=True, blank=True)
    job = models.CharField(max_length=8, null=True, blank=True)
    parrypct = models.CharField(max_length=8, null=True, blank=True)
    blockpct = models.CharField(max_length=8, null=True, blank=True)
    inctohit = models.CharField(max_length=8, null=True, blank=True)
    overhealpct = models.IntegerField(null=True, blank=True)

class DamageType(models.Model):
    class Meta:
        managed = False
        db_table = 'damagetype_table'

    encid = models.CharField(max_length=8, primary_key=True)
    combatant = models.CharField(max_length=64, null=True, blank=True)
    grouping = models.CharField(max_length=92, null=True, blank=True)
    type = models.CharField(max_length=64, null=True, blank=True)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    damage = models.IntegerField(null=True, blank=True)
    encdps = models.FloatField(null=True, blank=True)
    chardps = models.FloatField(null=True, blank=True)
    dps = models.FloatField(null=True, blank=True)
    average = models.FloatField(null=True, blank=True)
    median = models.IntegerField(null=True, blank=True)
    minhit = models.IntegerField(null=True, blank=True)
    maxhit = models.IntegerField(null=True, blank=True)
    hits = models.IntegerField(null=True, blank=True)
    crithits = models.IntegerField(null=True, blank=True)
    blocked = models.IntegerField(null=True, blank=True)
    misses = models.IntegerField(null=True, blank=True)
    swings = models.IntegerField(null=True, blank=True)
    tohit = models.FloatField(null=True, blank=True)
    averagedelay = models.FloatField(null=True, blank=True)
    critperc = models.CharField(max_length=8, null=True, blank=True)
    parrypct = models.CharField(max_length=8, null=True, blank=True)
    blockpct = models.CharField(max_length=8, null=True, blank=True)
    overheal = models.IntegerField(null=True, blank=True)


class Encounter(models.Model):
    class Meta:
        managed = False
        db_table = 'encounter_table'

    encid = models.CharField(max_length=8, primary_key=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    damage = models.IntegerField(null=True, blank=True)
    encdps = models.FloatField(null=True, blank=True)
    zone = models.CharField(max_length=64, null=True, blank=True)
    kills = models.IntegerField(null=True, blank=True)
    deaths = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{encid} - {title}".format(**self.__dict__)


class Swing(models.Model):
    class Meta:
        managed = False
        db_table = 'swing_table'

    encid = models.CharField(max_length=8, primary_key=True)
    stime = models.DateTimeField()
    attacker = models.CharField(max_length=64, null=True, blank=True)
    swingtype = models.IntegerField(null=True, blank=True)
    attacktype = models.CharField(max_length=64, null=True, blank=True)
    damagetype = models.CharField(max_length=64, null=True, blank=True)
    victim = models.CharField(max_length=64, null=True, blank=True)
    damage = models.IntegerField(null=True, blank=True)
    damagestring = models.CharField(max_length=128, null=True, blank=True)
    critical = models.CharField(max_length=1, null=True, blank=True)
    special = models.CharField(max_length=64, null=True, blank=True)
    dmgadjust = models.CharField(max_length=8, null=True, blank=True)
    dmgreduced = models.IntegerField(null=True, blank=True)
    overheal = models.IntegerField(null=True, blank=True)
