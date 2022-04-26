### Reusable Python class to send Slack messages via Webhooks



#### Usage

* Modify `slack_message_template.json` to add the channel you want to send messages to, customize your app icon, etc.
* Add an environment variable with your Slack webhook URL. e.g. `export SLACK_WEBHOOK_URL="https://test"`
* `python main.py`