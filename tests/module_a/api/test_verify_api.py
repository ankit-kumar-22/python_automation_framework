import pytest


@pytest.mark.api
def test_get_user(api_utils, config, custom_logger):
    response = api_utils.get(f"{config['api_base_url']}/fact")
    custom_logger.info(f"API Response code {response.status_code}")
    assert response.status_code == 200
