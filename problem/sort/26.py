import sys
import heapq

N = int(sys.stdin.readline().rstrip())
card = []
for _ in range(N):
    heapq.heappush(card,int(sys.stdin.readline().rstrip()))

result = 0

while N > 1:
    sum = heapq.heappop(card) + heapq.heappop(card) 
    heapq.heappush(card,sum)
    result += sum
    N -= 1
 
print(result)   
