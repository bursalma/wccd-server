class BaseAPI:
    name: str
    response: dict

    def test_get(self, client):
        res = client.get(f'/{self.name}')
        assert res.status_code == 308
        res = client.get(f'/{self.name}/')
        assert res.status_code == 200
        assert res.json == self.response
