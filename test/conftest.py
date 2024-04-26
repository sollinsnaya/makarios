from kritis import app

import pytest


@pytest.fixture()
def client():
    _app = app
    _app.config.update({
        'TESTING': True
    })

    return _app.test_client()
