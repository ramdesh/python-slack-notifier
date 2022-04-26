import os

from slack_notifier import SlackNotifier


def main():
    slack_webhook_url = os.environ.get("SLACK_WEBHOOK_URL", "https://my-slack-webhook")
    slack_notifier = SlackNotifier(slack_webhook_url)
    slack_notifier.send_slack_message("Your message here.")


if __name__ == "__main__":
    main()
