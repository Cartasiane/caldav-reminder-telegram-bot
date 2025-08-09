"""Tests that the bot starts with machine environment variables."""

import os
import subprocess
import sys
import time

import pytest


REQUIRED_ENV_VARS = [
    "CALDAV_URL",
    "CALDAV_USERNAME",
    "CALDAV_PASSWORD",
    "CALENDAR_IDS",
    "TELEGRAM_BOT_TOKEN",
    "TELEGRAM_CHAT_ID",
]

missing = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]


@pytest.mark.skipif(missing, reason=f"Missing environment variables: {', '.join(missing)}")
def test_bot_runs_with_machine_env():
    """Run the bot using machine environment variables and ensure it stays alive."""
    proc = subprocess.Popen([sys.executable, "-m", "src.app"], env=os.environ.copy())
    try:
        time.sleep(5)
        assert proc.poll() is None
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
