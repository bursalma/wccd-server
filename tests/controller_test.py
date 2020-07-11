class BaseAPI:
    name: str
    response: dict

    def test_get_redirect(self, client):
        res = client.get(f'/{self.name}')
        assert res.status_code == 308

    def test_get(self, client):
        res = client.get(f'/{self.name}/')
        assert res.status_code == 200


class TestNationalityAPI(BaseAPI):
    name = 'nationality'


class TestRaceAPI(BaseAPI):
    name = 'race'


class TestConvictAPI(BaseAPI):
    name = 'convict'


class TestConvictionAPI(BaseAPI):
    name = 'conviction'
