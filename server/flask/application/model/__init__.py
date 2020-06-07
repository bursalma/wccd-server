from typing import Dict, Union

class BaseModel:
    def get_dict(self) -> Dict[str, Union[str, int]]:
        dictret = dict((self.__dict__))
        dictret.pop('_sa_instance_state', None)

        # try:
        #     for ref in self.refs:
        #         try:
        #             dictret[ref] = dictret.get(ref).id
        #         except AttributeError:
        #             dictret[ref] = dictret.get(ref + '_id')
        #         dictret.pop(ref + '_id', None)       
        # except AttributeError: pass
        
        return dictret