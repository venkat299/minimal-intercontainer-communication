import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import service_a.app as service_a_app
import service_b.app as service_b_app


def test_service_a_ping():
    client = service_a_app.app.test_client()
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.get_json() == {'message': 'pong from service A'}


def test_service_b_call(monkeypatch):
    def fake_get(url, timeout):
        class DummyResp:
            def json(self):
                return {'message': 'pong from service A'}
        return DummyResp()

    monkeypatch.setattr(service_b_app.requests, 'get', fake_get)
    client = service_b_app.app.test_client()
    resp = client.get('/call')
    assert resp.status_code == 200
    assert resp.get_json() == {
        'caller': 'service_b',
        'service_a': 'pong from service A'
    }
