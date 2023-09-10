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

    def test_add_task_form(self):
        """
        Adding a task via the form adds it to the list of tasks
        """
        new_task_form_data = {
            "name": "Eat an apple",
            "description": "Buy an apple, wash an apple, eat an apple",
            "deadline": date.today(),
        }
        response = self.client.post(reverse("index"), data=new_task_form_data)

        # Check for redirection
        self.assertEqual(response.status_code, 302)

        # Follow the redirection
        response = self.client.get(response.url)

        self.assertContains(response, "Eat an apple")


def create_task(name, description, deadline, completed):
    return Task.objects.create(
        name=name, description=description, deadline=deadline, completed=completed
    )


class ToDoListIndexViewTests(TestCase):
    def test_overdue_does_not_show_when_no_deadline_supplied(self):
        task = create_task(
            "Make dinner", "Make dinner for the family", None, False
        )
        response = self.client.get(reverse("index"))
        self.assertNotContains(response, "Overdue")

    def test_edit_task_list_link(self):
        """
        Test that the link to edit a task is correct
        """
        task = create_task(
            "Make dinner", "Make dinner for the family", date.today(), True
        )
        response = self.client.get(reverse("index"))
        self.assertContains(response, f'<a href="/to-do/{task.id}"')
