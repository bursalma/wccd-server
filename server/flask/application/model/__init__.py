from typing import Dict, Union

class BaseModel:
    def get_dict(self) -> Dict[str, Union[str, int]]:
        dictret = dict((self.__dict__))
        dictret.pop('_sa_instance_state', None)
        return dictret