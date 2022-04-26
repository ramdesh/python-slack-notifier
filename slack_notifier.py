import json
import requests


class SlackNotifier:
    def __init__(self, slack_webhook_url: str):
        super().__init__()
        self.slack_webhook_url = slack_webhook_url

    def send_slack_message(self, message: str):
        with open("slack_message_template.json") as f:
            message_template = json.load(f)
        if len(message) > 39000:
            # Slack has a limit of 40000 chars, let's truncate it a bit
            message_to_send = (
                message[:39000] + "...(message too long for Slack, truncated.)"
            )
        else:
            message_to_send = message
        message_template["blocks"][0]["text"]["text"] = message_to_send
        requests.post(self.slack_webhook_url, json=message_template)
