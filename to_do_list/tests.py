from datetime import timedelta, date

from django.test import TestCase
from django.urls import reverse

from .models import Task


# Create your tests here.
class TaskModelTests(TestCase):
    def test_task_whose_deadline_has_passed_is_marked_as_overdue(self):
        """
        is_overdue() returns true when deadline is earlier than today
        """
        overdue_task = Task(deadline=date.today() - timedelta(days=1))
        self.assertIs(overdue_task.is_overdue(), True)

    def test_task_whose_deadline_is_in_the_future_is_marked_as_not_overdue(self):
        """
        is_overdue() returns true when deadline is earlier than today
        """
        overdue_task = Task(deadline=date.today() + timedelta(days=1))
        self.assertIs(overdue_task.is_overdue(), False)

    def test_task_whose_deadline_is_today_is_marked_as_not_overdue(self):
        """
        is_overdue() returns true when deadline is earlier than today
        """
        overdue_task = Task(deadline=date.today())
        self.assertIs(overdue_task.is_overdue(), False)


def create_task(name, description, deadline, completed):
	return Task.objects.create(name=name, description=description, deadline=deadline, completed=completed)


class ToDoListIndexViewTests(TestCase):
	def test_edit_task_list_link(self):
		"""
		The link to edit a task is correct
		"""
		task = create_task("Make dinner", "Make dinner for the family", date.today(), True)
		response = self.client.get(reverse("index"))
		self.assertContains(response, f'<a href="/to-do/{task.id}"')
		



