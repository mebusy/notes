import itertools
import heapq

REMOVED = '<removed-task>'      # placeholder for a removed task


class PriorityQueue():

    def __init__(self):
        self.pq = []                         # list of entries arranged in a heap
        self.entry_finder = {}               # mapping of tasks to entries
        self.counter = itertools.count()     # unique sequence count

    def push(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq :
            priority, count, task = heapq.heappop(self.pq)
            if task is not REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')

    def isEmpty(self):
        return len(self.pq) == 0


if __name__ == '__main__':
    import random

    for _ in range(1000):
        samples = random.sample(range(1000), k=60)
        s_min = min(samples)
        s_max = max(samples)
        pq = PriorityQueue()
        # print (pq.isEmpty())
        for v in samples :
            pq.push( v,v )
        assert s_min == pq.pop()
        # update
        pq.push( s_max , -3 )
        assert s_max == pq.pop()

