class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        R, C = len(grid) , len(grid[0])

        li = [0] * (C + 2)

        for item in grid:
            aLi = [0] + list(map(int,item)) + [0]
            li += aLi

        li += [0] * (C + 2)

        print(li)

        islands = 0

        def process(start):
            stack = [start]
            while stack:
                index = stack.pop()
                if li[index] != 1:
                    continue
                
                li[index] = 0

                if li[index - 1] == 1:
                    stack.append(index - 1)
                if li[index + 1] == 1:
                    stack.append(index + 1)
                if li[index - (C + 2)] == 1:
                    stack.append(index - (C + 2))
                if li[index + (C + 2)] == 1:
                    stack.append(index + (C + 2))

        for i in range(C + 3, (C + 2) * R + C + 1):
            if li[i] == 1:
                islands += 1
                process(i)

        return islands