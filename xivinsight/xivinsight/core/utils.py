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
