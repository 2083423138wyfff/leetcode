import sys

class Node:
    def __init__(self,key,value=None,pre=None,nxt=None):
        self.key=key
        self.value=value
        self.pre=pre
        self.nxt=nxt

class LRUcache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.hashmap={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.nxt=self.tail
        self.tail.pre=self.head
        
    def _add_to_head(self,node):#为什么前面要加_
        node.nxt=self.head.nxt
        node.pre=self.head
        self.head.nxt.pre=node
        self.head.nxt=node
        
    def _remove(self,node):
        node.pre.nxt=node.nxt
        node.nxt.pre=node.pre
    
    def get(self,key):
        if key not in self.hashmap:
            return -1
        node=self.hashmap[key]
        self._remove(node)
        self._add_to_head(node)
        return  node.value
        
    def put(self,key,value):
        if key in self.hashmap:
            node=self.hashmap[key]
            node.value=value
            self._remove(node)
            self._add_to_head(node)
        else:
            node=Node(key,value)
            self.hashmap[key]=node
            self._add_to_head(node)#这里怎么确定有头节点
            if len(self.hashmap)>self.capacity:
                last=self.tail.pre
                self._remove(last)
                del self.hashmap[last.key]#这个看不懂

def main():
    capacity=int(sys.stdin.readline().strip())
    cache=LRUcache(capacity)
    for line in sys.stdin:
        parts=line.split()
        if not parts:
            continue
        op=parts[0]
        if op=='put':
            cache.put(int(parts[1]),int(parts[2]))
        elif op =='get':
            print(cache.get(int(parts[1])))
            
if __name__=='__main__':
    main()