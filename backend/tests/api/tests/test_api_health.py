import pytest
import requests


@pytest.mark.smoke
def test_health(base_url):
    r = requests.get(f"{base_url}/health")
    assert r.status_code == 200
