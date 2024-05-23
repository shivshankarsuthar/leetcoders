class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(len(self.queue)):
            self.queue.append(self.queue[0])
            self.queue = self.queue[1:]

    def pop(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False

