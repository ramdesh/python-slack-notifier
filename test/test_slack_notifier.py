from unittest.mock import patch
import json

from slack_notifier import SlackNotifier


@patch("requests.post")
def test_slack_notifier_sends_message(requests_post_mock):
    test_webhook_url = "https://test"
    test_message = "Hello"
    with open("slack_message_template.json") as f:
        message_template = json.load(f)
    message_template["blocks"][0]["text"]["text"] = test_message
    slack_notifier = SlackNotifier(test_webhook_url)
    slack_notifier.send_slack_message(test_message)

    requests_post_mock.assert_called_with(test_webhook_url, json=message_template)
