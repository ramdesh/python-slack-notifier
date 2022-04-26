### Reusable Python class to send Slack messages via Webhooks

As described [here](https://rsdeshapriya.com/a-reusable-python-class-for-sending-slack-messages-c06f8f2818d5).

#### Usage

* `pip install -r requirements.txt` (note that if you are using this class in other applications, you will have to include the `requests` library as part of your dependencies.
* Modify `slack_message_template.json` to add the channel you want to send messages to, customize your app icon, etc.
* Add an environment variable with your Slack webhook URL. e.g. `export SLACK_WEBHOOK_URL="https://test"`
* `python main.py`

#### Development

* `pip install -r requirements.dev.txt`
* `pytest`
