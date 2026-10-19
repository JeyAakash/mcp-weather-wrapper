import pytest
from server import get_current_weather, get_weather_forecast

def test_get_current_weather_valid():
    result = get_current_weather("London")
    assert isinstance(result, str)
    assert len(result) > 0

def test_get_current_weather_empty_city():
    with pytest.raises(ValueError, match="City name cannot be empty"):
        get_current_weather("")

def test_get_forecast_invalid_days():
    with pytest.raises(ValueError, match="Days must be between 1 and 3"):
        get_weather_forecast("London", days=5)

def test_get_forecast_empty_city():
    with pytest.raises(ValueError, match="City name cannot be empty"):
        get_weather_forecast("", days=2)
    