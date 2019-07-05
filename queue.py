from collections import deque
queue = deque(["a", "b", "c"])
queue.append("d")           # Terry arrives
queue.append("e")# Graham arrives
print(queue)
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
print(queue)                           # Remaining queue in order of arrival
#deque(['Michael', 'Terry', 'Graham'])
