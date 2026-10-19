import pytest
from server import get_current_weather, daily_briefing

def test_get_current_weather_valid():
    """Test that get_current_weather returns a string response for a valid city."""
    result = get_current_weather("Tokyo")
    assert isinstance(result, str)
    assert "Tokyo" in result

def test_daily_briefing_valid():
    """Test that daily_briefing returns a proper briefing for a valid city."""
    result = daily_briefing("London")
    assert isinstance(result, str)
    assert "London" in result
