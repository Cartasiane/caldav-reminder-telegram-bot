import caldav
from datetime import datetime
import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from src.app import Reminder


def test_reminder_can_be_instantiated():
    """Reminder dataclass should allow optional valarm after vevent."""
    vevent = caldav.vobject.base.Component("VEVENT")
    reminder = Reminder(dt=datetime.now(), vevent=vevent)
    assert reminder.vevent is vevent
    assert reminder.valarm is None
