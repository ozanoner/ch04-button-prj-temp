import os
import time
from typing import Any

import pexpect
import pytest

BUTTON_ID = "btn1"
BUTTON_CONTROL = "pressed"
APP_PATH = os.path.dirname(__file__)


def _tap_button(wokwi: Any, duration_ms: int = 100) -> None:
    wokwi.client.set_control(BUTTON_ID, BUTTON_CONTROL, 1)
    time.sleep(duration_ms / 1000)
    wokwi.client.set_control(BUTTON_ID, BUTTON_CONTROL, 0)


def _hold_button(wokwi: Any, duration_ms: int) -> None:
    wokwi.client.set_control(BUTTON_ID, BUTTON_CONTROL, 1)
    time.sleep(duration_ms / 1000)
    wokwi.client.set_control(BUTTON_ID, BUTTON_CONTROL, 0)


@pytest.mark.generic
@pytest.mark.parametrize("app_path", [APP_PATH], indirect=True)
@pytest.mark.parametrize("target", ["esp32", "esp32c3"], indirect=True)
@pytest.mark.parametrize("config", ["config1", "config2"], indirect=True)
def test_button_behaviors(dut: Any, wokwi: Any, config: str) -> None:
    del config
    dut.expect("button gpio num:", timeout=10)

    _tap_button(wokwi, duration_ms=150)
    dut.expect("single-click", timeout=5)
    time.sleep(3.0)


    long_press_duration_ms = int(dut.app.sdkconfig.get("BUTTON_LONG_PRESS_TIME_MS", 1500))
    press_margin_ms = 200

    hold_time = long_press_duration_ms + press_margin_ms
    _hold_button(wokwi, hold_time)
    dut.expect("long-press", timeout=5)
