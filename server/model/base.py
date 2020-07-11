from datetime import datetime
from typing import Dict, Union

now = datetime.utcnow


class BaseModel:
    def get_dict(self) -> Dict[str, Union[str, int]]:
        """Modify the model's dict to return in dict type."""
        dictret = dict((self.__dict__))
        dictret.pop('_sa_instance_state', None)
        return dictret
