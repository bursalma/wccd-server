from datetime import datetime

from .. import db

now = datetime.utcnow


class BaseModel:
    """Base class to define dynamic attributes and methods for all models."""

    _models: dict = {}
    _fields: list = []
    _ATTRS: list = ['__module__', '__tablename__', 'id', 'last_update',
                    '__doc__', '__table__', '_sa_class_manager', '__init__',
                    '__mapper__']

    @classmethod
    def models(cls) -> dict:
        """Virtually initialize a models dictionary
        that maps models to their name.
        """
        if not cls._models:
            dictret = dict(db.Model._decl_class_registry)
            dictret.pop('_sa_module_registry', None)
            cls._models = dictret
        return cls._models

    @classmethod
    def fields(cls) -> list:
        """Virtually initialize a fields list."""
        if not cls._fields:
            dictret = dict(cls.__dict__)
            for attr in cls._ATTRS:
                dictret.pop(attr, None)

            cls._fields = [key for key in dictret if key[:4] != 'all_']
        return cls._fields

    def get_dict(self) -> dict:
        """Modify the model's dict to return in dict type."""
        dictret = dict((self.__dict__))
        dictret.pop('_sa_instance_state', None)
        return dictret
