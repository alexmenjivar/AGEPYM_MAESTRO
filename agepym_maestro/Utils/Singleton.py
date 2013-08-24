'''
Created on 15/08/2013

@author: Lennin
'''

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def borrar(cls):
        Singleton._instance = None