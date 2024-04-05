def test_ok(client):
    res = client.get('/')

    assert res.status_code == 200
    assert b'Convert an image to a paint by numbers' in res.data
