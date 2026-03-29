from datetime import date
from pawpal_system import Owner, Dog, Cat, Task, Scheduler

# ---------------------------------------------------------------------------
# 1. Create Owner
# ---------------------------------------------------------------------------
owner = Owner(name="Alex")

owner.availability = {
    "Sunday": {
        "early_morning": 30,
        "lunch_break":   60,
        "afternoon":     45,
        "evening":       60,
    },
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
    "Sunday":  "early_morning",
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
buddy.tasks = [
    Task(name="Morning walk",     category="exercise",     duration=30, priority="high",   time_slot="early_morning", frequency="once"),
    Task(name="Breakfast",        category="eating",       duration=15, priority="high",   time_slot="early_morning", frequency="once"),
    Task(name="Fish oil vitamin", category="routine_med",  duration=5,  priority="medium", time_slot="early_morning", frequency="once"),
    Task(name="Afternoon walk",   category="exercise",     duration=30, priority="medium", time_slot="afternoon",     frequency="once"),
    Task(name="Dinner",           category="eating",       duration=15, priority="high",   time_slot="evening",       frequency="once"),
]

luna.tasks = [
    Task(name="Breakfast",           category="eating",    duration=10, priority="high",   time_slot="early_morning", frequency="once"),
    Task(name="Litter box cleaning", category="grooming",  duration=10, priority="medium", time_slot="early_morning", frequency="once"),
    Task(name="Playtime",            category="enrichment",duration=20, priority="medium", time_slot="afternoon",     frequency="once"),
    Task(name="Dinner",              category="eating",    duration=10, priority="high",   time_slot="evening",       frequency="once"),
]

# ---------------------------------------------------------------------------
# 4. Run Scheduler — separate schedule per pet
# ---------------------------------------------------------------------------
today = date.today()
scheduler = Scheduler(owner=owner, pets=[buddy, luna])

SLOTS = ["early_morning", "lunch_break", "afternoon", "evening"]
SLOT_LABELS = {
    "early_morning": "Early Morning",
    "lunch_break":   "Lunch Break",
    "afternoon":     "Afternoon",
    "evening":       "Evening",
}

def print_pet_schedule(pet, daily, flagged):
    print(f"\n{'=' * 50}")
    print(f"  {pet.name} ({pet.__class__.__name__}) — {daily.day_of_week}, {today}")
    print(f"{'=' * 50}")
    for slot in SLOTS:
        tasks = daily.time_slots.get(slot, [])
        print(f"\n  [{SLOT_LABELS[slot]}]")
        if tasks:
            for t in tasks:
                status = "✓" if t.completed else "○"
                print(f"    {status} {t.name:<25} | {t.duration:>3} min | priority: {t.priority}")
        else:
            print("    — no tasks scheduled —")

    scheduled = len(daily.tasks)
    print(f"\n  Scheduled {scheduled} task(s).")
    if flagged:
        print("  ⚠ Flagged tasks (could not be scheduled):")
        for t in flagged:
            print(f"    • {t.name} ({t.priority} priority, {t.duration} min)")
    print(f"{'=' * 50}")

# ---------------------------------------------------------------------------
# 5. Print each pet's schedule separately
# ---------------------------------------------------------------------------
print("\n  PawPal+ — Today's Schedule\n")

for pet in [buddy, luna]:
    scheduler.flagged_tasks = []  # reset flags per pet
    daily = scheduler.generate_daily_schedule_for_pet(pet, today)
    print_pet_schedule(pet, daily, scheduler.flagged_tasks)

# ---------------------------------------------------------------------------
# 6. Conflict Detection Demo
# ---------------------------------------------------------------------------
print("\n  Conflict Detection")
print("=" * 50)
today_name = today.strftime("%A")
for pet in [buddy, luna]:
    conflicts = scheduler.detect_conflicts(pet, today_name)
    if conflicts:
        for warning in conflicts:
            print(f"  {warning}")
    else:
        print(f"  No conflicts detected for {pet.name}.")
print("=" * 50)