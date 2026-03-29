from datetime import date
from pawpal_system import Owner, Dog, Cat, Task, Scheduler

# ---------------------------------------------------------------------------
# 1. Create Owner
# ---------------------------------------------------------------------------
owner = Owner(name="Alex")

owner.availability = {
    "Monday": {
        "early_morning": 30,
        "lunch_break":   60,
        "afternoon":     45,
        "evening":       60,
    },
    "Tuesday": {
        "early_morning": 20,
        "lunch_break":   30,
        "afternoon":     60,
        "evening":       90,
    },
}

owner.preferred_slots = {
    "Monday":  "early_morning",
    "Tuesday": "evening",
}

# ---------------------------------------------------------------------------
# 2. Create Pets
# ---------------------------------------------------------------------------
buddy = Dog(
    name="Buddy",
    age=3,
    owner=owner,
    breed="Golden Retriever",
    birthday=date(2022, 4, 10),
    vet_info="Dr. Paws Clinic — (626) 555-0192",
    health_notes="No known conditions. Daily fish oil supplement.",
)

luna = Cat(
    name="Luna",
    age=5,
    owner=owner,
    breed="Domestic Shorthair",
    birthday=date(2020, 8, 22),
    vet_info="Dr. Paws Clinic — (626) 555-0192",
    health_notes="Sensitive stomach. Grain-free diet recommended.",
)

# ---------------------------------------------------------------------------
# 3. Add Tasks to Pets
# ---------------------------------------------------------------------------

# Buddy's tasks
buddy.tasks = [
    Task(name="Morning walk",    category="exercise",     duration=30, priority="high",   time_slot="early_morning", frequency="once"),
    Task(name="Breakfast",       category="eating",       duration=15, priority="high",   time_slot="early_morning", frequency="once"),
    Task(name="Fish oil vitamin", category="routine_med", duration=5,  priority="medium", time_slot="early_morning", frequency="once"),
    Task(name="Afternoon walk",  category="exercise",     duration=30, priority="medium", time_slot="afternoon",     frequency="once"),
    Task(name="Dinner",          category="eating",       duration=15, priority="high",   time_slot="evening",       frequency="once"),
]

# Luna's tasks
luna.tasks = [
    Task(name="Breakfast",          category="eating",    duration=10, priority="high",   time_slot="early_morning", frequency="once"),
    Task(name="Litter box cleaning", category="grooming", duration=10, priority="medium", time_slot="early_morning", frequency="once"),
    Task(name="Playtime",           category="enrichment",duration=20, priority="medium", time_slot="afternoon",     frequency="once"),
    Task(name="Dinner",             category="eating",    duration=10, priority="high",   time_slot="evening",       frequency="once"),
]

# ---------------------------------------------------------------------------
# 4. Run Scheduler for Today
# ---------------------------------------------------------------------------
today = date.today()
scheduler = Scheduler(owner=owner, pets=[buddy, luna])
daily = scheduler.generate_daily_schedule(schedule_date=today)

# ---------------------------------------------------------------------------
# 5. Print Today's Schedule
# ---------------------------------------------------------------------------
SLOTS = ["early_morning", "lunch_break", "afternoon", "evening"]
SLOT_LABELS = {
    "early_morning": "Early Morning",
    "lunch_break":   "Lunch Break",
    "afternoon":     "Afternoon",
    "evening":       "Evening",
}

print("=" * 50)
print(f"  PawPal+ — Today's Schedule ({daily.day_of_week}, {today})")
print("=" * 50)

for slot in SLOTS:
    tasks = daily.time_slots.get(slot, [])
    print(f"\n  [{SLOT_LABELS[slot]}]")
    if tasks:
        for t in tasks:
            status = "✓" if t.completed else "○"
            print(f"    {status} {t.name:<25} | {t.duration:>3} min | priority: {t.priority}")
    else:
        print("    — no tasks scheduled —")

print("\n" + "=" * 50)
print(f"  {scheduler.explain_plan()}")

if scheduler.flagged_tasks:
    print("\n  ⚠ Flagged tasks (could not be scheduled):")
    for t in scheduler.flagged_tasks:
        print(f"    • {t.name} ({t.priority} priority, {t.duration} min)")

print("=" * 50)
