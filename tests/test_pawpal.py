import pytest
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


# ---------------------------------------------------------------------------
# Test 1: Task Completion
# Verify that calling mark_complete() changes the task's status to True
# ---------------------------------------------------------------------------
def test_mark_complete(sample_task):
    assert sample_task.completed is False       # starts incomplete
    sample_task.mark_complete()
    assert sample_task.completed is True        # should now be complete


# ---------------------------------------------------------------------------
# Test 2: Task Addition
# Verify that adding a task to a Pet increases that pet's task count
# ---------------------------------------------------------------------------
def test_add_task_increases_count(dog, sample_task):
    initial_count = len(dog.tasks)
    dog.tasks.append(sample_task)
    assert len(dog.tasks) == initial_count + 1