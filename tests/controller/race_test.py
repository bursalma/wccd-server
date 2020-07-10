from . import BaseAPI


class TestRaceAPI(BaseAPI):
    name = 'race'
    response = {
        "race": [
            {
                "id": 1,
                "last_update": "Wed, 08 Jul 2020 04:18:10 GMT",
                "race": "Asian"
            },
            {
                "id": 2,
                "last_update": "Wed, 08 Jul 2020 04:18:10 GMT",
                "race": "Black"
            },
            {
                "id": 3,
                "last_update": "Wed, 08 Jul 2020 04:18:10 GMT",
                "race": "Hispanic"
            },
            {
                "id": 4,
                "last_update": "Wed, 08 Jul 2020 04:18:10 GMT",
                "race": "White"
            },
            {
                "id": 5,
                "last_update": "Wed, 08 Jul 2020 04:18:10 GMT",
                "race": "Other"
            },
            {
                "id": 6,
                "last_update": "Wed, 08 Jul 2020 04:18:10 GMT",
                "race": "NOT REPORTED"
            }
        ]
    }
