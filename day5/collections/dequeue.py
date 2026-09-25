from collections import deque
# add task 4 to the right and add urgent task to the left and remove one item from each side
tasks=["Task1","Task2","task3"]
queue=deque(tasks)
queue.append("Task4")
queue.appendleft("UrgentTask")

print(list(queue))


queue.pop()
queue.popleft()

print(list(queue))