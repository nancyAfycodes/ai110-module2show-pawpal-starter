import pytest
from datetime import date, timedelta
from pawpal_system import Owner, Dog, Cat, Task


# ---------------------------------------------------------------------------
# Fixtures — reusable test setup
# ---------------------------------------------------------------------------
@pytest.fixture
def owner():
    return Owner(name="Test Owner")


@pytest.fixture
def dog(owner):
    return Dog(name="Buddy", age=3, owner=owner, breed="Golden Retriever")


@pytest.fixture
def sample_task():
    return Task(
        name="Morning walk",
        category="exercise",
        duration=30,
        priority="high",
        time_slot="early_morning",
        frequency="once",
    )


@pytest.fixture
def daily_task():
    return Task(
        name="Breakfast",
        category="eating",
        duration=10,
        priority="high",
        time_slot="early_morning",
        frequency="daily",
        due_date=date.today(),
    )


@pytest.fixture
def weekly_task():
    return Task(
        name="Grooming",
        category="grooming",
        duration=20,
        priority="medium",
        time_slot="afternoon",
        frequency="weekly",
        due_date=date.today(),
    )


# ---------------------------------------------------------------------------
# Test 1: Task Completion — once
# Verify that mark_complete() changes status and returns None for a one-off task
# ---------------------------------------------------------------------------
def test_mark_complete_once(sample_task):
    assert sample_task.completed is False
    result = sample_task.mark_complete()
    assert sample_task.completed is True
    assert result is None                   # no recurrence for "once" tasks


# ---------------------------------------------------------------------------
# Test 2: Task Addition
# Verify that adding a task to a Pet increases that pet's task count
# ---------------------------------------------------------------------------
def test_add_task_increases_count(dog, sample_task):
    initial_count = len(dog.tasks)
    dog.tasks.append(sample_task)
    assert len(dog.tasks) == initial_count + 1


# ---------------------------------------------------------------------------
# Test 3: Recurring task — daily
# Verify that mark_complete() returns a new Task due tomorrow
# ---------------------------------------------------------------------------
def test_mark_complete_daily(daily_task):
    next_task = daily_task.mark_complete()
    assert daily_task.completed is True
    assert next_task is not None
    assert next_task.due_date == date.today() + timedelta(days=1)
    assert next_task.completed is False     # new task starts incomplete


# ---------------------------------------------------------------------------
# Test 4: Recurring task — weekly
# Verify that mark_complete() returns a new Task due in 7 days
# ---------------------------------------------------------------------------
def test_mark_complete_weekly(weekly_task):
    next_task = weekly_task.mark_complete()
    assert weekly_task.completed is True
    assert next_task is not None
    assert next_task.due_date == date.today() + timedelta(weeks=1)
    assert next_task.completed is False     # new task starts incomplete