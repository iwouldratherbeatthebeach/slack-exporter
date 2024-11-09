#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pathlib import Path

# Get the directory containing the setup.py file
base_dir = Path(__file__).resolve().parent

# Read requirements from the requirements.txt file
def parse_requirements(filename):
    requirements_path = base_dir / filename
    with requirements_path.open("r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        requires = []
        links = []
        for line in lines:
            if line.startswith("#") or not line.strip():
                continue
            if line.startswith("-e") or "://" in line:
                links.append(line)
            else:
                requires.append(line)
        return requires, links

requires, links = parse_requirements("requirements.txt")

config = {
    "description": "Export messages from Slack conversations",
    "author": "Your Name",
    "url": "https://github.com/your-repo/slack-exporter",
    "version": "1.0.0",
    "packages": find_packages(),
    "scripts": [str(base_dir / "bin" / "slack-exporter.py")],
    "name": "slack-exporter",
    "install_requires": requires,
    "dependency_links": links,
}

setup(**config)