class Queue():
    """ Queue data structure """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Cannot dequeue from empty queue")
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def to_string(self):
        from functools import reduce
        return reduce(lambda x, y: str(x) + " " + str(y), self.items).strip()

    def __str__(self):
        return self.to_string()
