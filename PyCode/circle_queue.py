class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.max_size = k
        self.queue = [ -1 for i in range(k)]
        self.front = -1
        self.rear = -1
        self.length = 0
        
    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull() is True:
            return False
        if self.isEmpty() is True:
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        self.length += 1
        return True
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty() is True :
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
            self.length = 0
        else:
            self.front = (self.front + 1) % self.max_size
            self.length -= 1
        return True
            

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[self.front]
        return -1

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[self.rear]
        return -1
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.length == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.length == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()