class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # pq = [(1,1),(1,3),]
        graph = {}

        for i in range(1, n+1):
            graph[i] = []
        
        for a,b,t in times:
            graph[a].append((b,t))
        
        pq = []
        done_set = set()
        heapq.heappush(pq,(0,k))
        
        while pq:
            cur_time, node = heapq.heappop(pq)

            if node in done_set:
                continue
            
            done_set.add(node)

            if len(done_set) == n:
                return cur_time

            for b,t in graph[node]:
                if b in done_set:
                    continue
                heapq.heappush(pq,(cur_time + t, b))
        return -1