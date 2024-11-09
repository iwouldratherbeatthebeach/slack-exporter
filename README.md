## Slack Exporter

This Python script allows you to export messages from your Slack conversations. It supports fetching public channels, private channels, direct messages (DMs), and group DMs (MPIMs) based on the scopes available in your Slack user token.

## Features

- Export messages from public and private channels.
- Optionally export messages from DMs and group DMs if your token has the necessary permissions.
- Specify a date range for message history.
- Save conversations and messages as JSON files.

## Requirements

- Python 3.6 or higher
- Slack user token (`xoxe.xoxp-...`)

## Installation

Install the dependencies via setup.py

Run the script with the following command:

python slack-exporter.py --messages --scope public_channel,private_channel --date-start 2020-01-01 --date-end 2024-11-07

## Arguments
--data: Directory to save the exported data (default: data).
--messages: Export messages from conversations.
--scope: Type of conversations to fetch. Options include:
public_channel: Public channels.
private_channel: Private channels.
im: Direct messages.
mpim: Group direct messages.
Combine scopes with commas, e.g., public_channel,private_channel.
--date-start: Start date for message history (format: YYYY-MM-DD).
--date-end: End date for message history (format: YYYY-MM-DD).

## Example
Export messages from public and private channels within a date range:

python slack-exporter.py --messages --scope public_channel,private_channel --date-start 2020-01-01 --date-end 2024-11-07

## Author and Acknowledgments
This script was adapted from work by Lee Archer and modified to use the slack_sdk for enhanced functionality.
