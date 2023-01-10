class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(curr):
            if curr == destination:
                return True
            if not visited[curr]:
                visited[curr] = True
                for next_node in graph[curr]:
                    if dfs(next_node):
                        return True
            return False
        
        # convert graph to an adjacency list 
        graph = collections.defaultdict(list)             
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        visited = n*[False]
        
        return dfs(source)
        
        
            
            
        