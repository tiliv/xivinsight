from datetime import timedelta

SWING_TYPES = {
    'AUTO_ATTACK': 1,
    'SKILL': 2,
    '???': 10,
    'DOT_TICK': 20,
    'NEW_EFFECT': 21,
}
SWING_TYPES_CHOICES = (
    (SWING_TYPES['AUTO_ATTACK'], "Auto-attack"),
    (SWING_TYPES['SKILL'], "Skill"),  # GCD and Instant skills both show as 2
    (SWING_TYPES['???'], "(Instant?)"),
    (SWING_TYPES['DOT_TICK'], "DoT tick"),
    (SWING_TYPES['NEW_EFFECT'], "New effect"),  # damagestring becomes an aggro quantity
)

def annotate_timestamp_deltas(object_list, timestamp_field):
    object_list = list(object_list)
    last_timestamp = None
    for obj in object_list:
        timestamp = getattr(obj, timestamp_field)
        if last_timestamp is None:
            delta = timedelta()  # 0
        else:
            delta = timestamp - last_timestamp
        setattr(obj, "{}_delta".format(timestamp_field), delta)
        last_timestamp = timestamp
    return object_list
