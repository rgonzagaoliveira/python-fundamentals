#!/usr/bin/python

class Client:
    _id = 0
    _name = ""
    _cpf = ""
    _segment = ""

    def __init__(self,name="",cpf="",segment=""):
        self._name = name
        self._cpf = cpf
        self._segment = segment
