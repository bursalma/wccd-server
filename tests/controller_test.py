class BaseAPI:
    name: str
    response: dict

    def test_get_status(self, client):
        res = client.get(f'/{self.name}')
        assert res.status_code == 308

        res = client.get(f'/{self.name}/')
        assert res.status_code == 200


class TestNationalityAPI(BaseAPI):
    name = 'nationality'

    def test_turkish(self, client):
        res = client.get(f'/{self.name}/')
        assert res.json[self.name][182][self.name] == 'Turkish'


class TestRaceAPI(BaseAPI):
    name = 'race'

    def test_white(self, client):
        res = client.get(f'/{self.name}/')
        assert res.json[self.name][3][self.name] == 'White'


class TestConvictAPI(BaseAPI):
    name = 'convict'

    def test_bursal_modify(self, client):
        res = client.post(f'/{self.name}', json={'last_name': 'bursal'})
        assert res.json['last_name'] == 'bursal'

        res = client.put(f'/{self.name}/{res.json["id"]}',
                         json={'last_name': 'bursalnew'})
        assert res.json['last_name'] == 'bursalnew'

        res = client.delete(f'/{self.name}/{res.json["id"]}')
        assert res.status_code == 200

        res = client.get(f'/{self.name}/')
        assert res.json[self.name] == []


class TestConvictionAPI(BaseAPI):
    name = 'conviction'

    def test_bursal_modify(self, client):
        # res2 = client.post('/convict', json={'last_name': 'bursal'})
        # assert res2.json['last_name'] == 'bursal'

        res = client.post(f'/{self.name}', json={
            'company': 'Cognizant', 'convict_id': 1})
        assert res.json['company'] == 'Cognizant'

        # assert res.json['convict_id'] == 1
        # print(res.json)
        # res2 = client.get('/convict/')
        # print(res2.json)

        # res2 = client.get(f'/convict/{res.json["convict_id"]}')
        # assert res2.json['last_name'] == 'bursal'

        res = client.put(f'/{self.name}/{res.json["id"]}',
                         json={'company': 'HBO'})
        assert res.json['company'] == 'HBO'
