#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: slack-exporter
Description: Export messages from Slack conversations based on user-specified scope.
"""

import os
import sys
import json
import argparse
from datetime import datetime, date
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Add your Slack user token here
SLACK_TOKEN = "xoxe.xoxp-..."  # Replace with your actual token

class SlackExporter:
    def __init__(self, token, data_dir):
        self.client = WebClient(token=token)
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)

    def fetch_conversations(self, scope):
        """Fetch conversations based on the specified scope."""
        try:
            response = self.client.conversations_list(types=scope)
            conversations = response['channels']
            with open(os.path.join(self.data_dir, "conversations.json"), "w") as f:
                json.dump(conversations, f)
            print(f"Exported {len(conversations)} conversations.")
            return conversations
        except SlackApiError as e:
            print(f"Error fetching conversations: {e.response['error']}")
            sys.exit(1)

    def fetch_messages(self, channel_id, channel_name, date_start, date_end):
        """Fetch messages from a specific channel."""
        messages = []
        oldest = datetime.strptime(date_start, "%Y-%m-%d").timestamp()
        latest = datetime.strptime(date_end, "%Y-%m-%d").timestamp()

        try:
            while True:
                response = self.client.conversations_history(
                    channel=channel_id, oldest=oldest, latest=latest, limit=200
                )
                messages.extend(response['messages'])
                if not response.get('has_more', False):
                    break

            with open(os.path.join(self.data_dir, f"{channel_name}.json"), "w") as f:
                json.dump(messages, f)
            print(f"Exported {len(messages)} messages from {channel_name}.")
        except SlackApiError as e:
            print(f"Error fetching messages from {channel_name}: {e.response['error']}")

def main():
    token = SLACK_TOKEN
    if not token:
        print("Please provide a Slack token via SLACK_TOKEN in the script.", file=sys.stderr)
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Fetch messages from Slack conversations.")
    parser.add_argument("--data", type=str, default="data", help="Directory to save the data")
    parser.add_argument("--messages", action="store_true", help="Export messages from conversations")
    parser.add_argument("--scope", type=str, default="public_channel", 
                        help="Scope of conversations to fetch (e.g., public_channel, private_channel, im, mpim, or a combination separated by commas)")
    parser.add_argument("--date-start", default="2023-01-01", help="Start date for message history (YYYY-MM-DD)")
    parser.add_argument("--date-end", default=str(date.today()), help="End date for message history (YYYY-MM-DD)")

    args = parser.parse_args()

    exporter = SlackExporter(token, args.data)

    if args.messages:
        # Fetch conversations based on the specified scope
        conversations = exporter.fetch_conversations(args.scope)

        # Fetch messages for each conversation
        for convo in conversations:
            exporter.fetch_messages(convo['id'], convo['name'], args.date_start, args.date_end)

if __name__ == "__main__":
    main()
