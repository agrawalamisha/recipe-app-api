"""
Test customDjango management commands.
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2OpError

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


# we want to mock the behaviour of the database- added path for command
# we'll be mocking patch adds a mocked object in each function call.
# we're catching that in patched_check argument
@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test Commands"""

    def test_wait_for_db_ready(self, patched_check):
        """ test command waiting for db if db is ready."""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    # add another mocked object to mimic the sleep method with no wait for
    # quicker execution of testcase note, we're mocking this object only
    # for this method
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """ test waiting for db when getting operational error """
        # patched_check object will raise Psycopg2OpError first 2 times,
        # OperationalError next 3 times, and finally return True
        patched_check.side_effect = [Psycopg2OpError] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        # patched_check should be called exactly 6 times for this test case
        self.assertEquals(patched_check.call_count, 6)
        # note: assert_called_with diff from assert_called_once_with in
        # test_wait_for_db_ready method
        patched_check.assert_called_with(databases=['default'])
