class BaseAPI:
    name: str
    response: dict

    def test_get_redirect(self, client):
        res = client.get(f'/{self.name}')
        assert res.status_code == 308

    def test_get(self, client):
        res = client.get(f'/{self.name}/')
        assert res.status_code == 200
