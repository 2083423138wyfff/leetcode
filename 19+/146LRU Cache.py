import sys
class Node():
    def __init__(self,key,value,pre=None,nxt=None):
        self.key=key
        self.value=value
        self.pre=pre
        self.nxt=nxt
class LRUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.hashmap={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.nxt=self.tail
        self.tail.pre=self.head
        
    def _add_node(self,node):
        node.pre=self.head
        node.nxt=self.head.nxt
        self.head.nxt.pre=node
        self.head.nxt=node
        
    def _remove_node(self,node):
        self.tail.pre=node.pre
        node.pre.nxt=self.tail
        
    def put(self,key,value):
        if value not in self.hashmap:
            node=Node(key,value)
            self._add_node(node)
            self.hashmap[key]=node
            if len(self.hashmap)>self.capacity:
                _remove_node(self.tail.pre)
                del self.hashmap[self.tail.pre.key]
        else:
            node=Node(key,value)
            node.value=self.hashmap[key]#这是旧的
            
            
    def get(self,key):
        if key not in self.hashmap:
            return -1
        node=self.hashmap[key]
        self._remove_node(node)
        self._add_node(node)
        return node.value
    