import unittest
from unittest.mock import patch

from gorillassite.business.action import SendMessage
from tests import util


__author__ = 'abreu'


class SendMessageTestCase(unittest.TestCase):

    @patch('gorillassite.business.integration.slack.Slack', autospec=True)
    def test_sucesso(self, mock_slack):

        action = SendMessage(mock_slack)

        action.add_parameter(**util.dict_contato())

        action.execute()

        self.assertEqual(mock_slack.send_message.call_count, 1)
