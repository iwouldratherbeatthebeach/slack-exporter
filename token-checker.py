from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

token = "xoxe.xoxp-..."  # Your full token here
client = WebClient(token=token)

try:
    response = client.auth_test()
    print(response)  # Should show workspace details if valid
except SlackApiError as e:
    print(f"Auth error: {e.response['error']}")
