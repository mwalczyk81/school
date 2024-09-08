import heapq

class MinHeap:
    heapq_module = heapq

    def __init__(self):
        self.heap = []

    def insert(self, element):
        self.heapq_module.heappush(self.heap, element)

    def extract_min(self):
        if not self.heap:
            return None
        return self.heapq_module.heappop(self.heap)

    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]