#!/usr/bin/python3

class Node:
    def __init__(self, data=0, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an intege")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
     def next_node(self, value):
         if not isinstance(value, Node):
             raise TypeError("next_node must be a Node object")
         self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head  = None


