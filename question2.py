# Question 2: Queue Using Two Stacks

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:  # if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Dequeue from empty queue")
        return self.stack2.pop() # last item return


# Example Usage
if __name__ == "__main__":
    
    queue = QueueUsingStacks()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Dequeued:", queue.dequeue())