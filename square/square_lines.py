from math import *

class Solution:
    
    file = open('square.txt')

    def __init__(self):
        self.vals = []
        self.number = None
        
        vals = self.file.readline().split()

        if len(vals) > 1:
            self.number = int(vals[len(vals)-1])
            vals.pop()
        for i in range(0, len(vals)):
            vals[i] = float(vals[i])
        if vals[0] == vals[2] and vals[1] == vals[3]:
            print('[*] ERR, initialization is incorrect. Data in square.txt was wrong')
            return 0
        else:
            self.vals = vals
    
    def rate_space(self):
        if self.vals[0] == 0:
            if self.vals[2] < 1:
                space = 0.5*(1-self.vals[1])*self.vals[2]
                return space/(1-space)
            space_1 = 0.5*(2 - self.vals[1] - self.vals[3])
            space_2 = 0.5*(self.vals[1]+self.vals[3])
            return min(space_1, space_2)/max(space_1, space_2)
        elif self.vals[1] == 0:
            if self.vals[3] < 1:
                space = 0.5*(1-self.vals[0])*self.vals[3]
                return space/(1-space)
            space_1 = 0.5*(vals[0] + vals[2])
            space_2 = 0.5*(2 - self.vals[0] - self.vals[2])
            return min(space_1, space_2)/max(space_1, space_2)
        return 0

    def intersections(self, objects):
        inter = {}
        if self in objects:
            print('[*] ERR, division by zero')
            return 0
        else:
            for i in range(0, len(objects)):
                if (objects[i].vals[1] - objects[i].vals[3])/(objects[i].vals[0] - objects[i].vals[2]) == (self.vals[1] - self.vals[3])/(self.vals[0] - self.vals[2]):
                    pass
                else:
                    x = ((objects[i].vals[1] - objects[i].vals[3])/(objects[i].vals[0] - objects[i].vals[2]) * objects[i].vals[0] - (self.vals[1] - self.vals[3])/(self.vals[0] - self.vals[2]) * self.vals[0] + self.vals[1] - objects[i].vals[1])/((objects[i].vals[1] - objects[i].vals[3])/(objects[i].vals[0] - objects[i].vals[2]) - (self.vals[1] - self.vals[3])/(self.vals[0] - self.vals[2]))
                    y = (self.vals[1] - self.vals[3])/(self.vals[0] - self.vals[2]) * (x - self.vals[0]) + self.vals[1]
                    if x<=1 and y<=1:
                        xy = [x, y]
                        inter[str(self.number) + str(objects[i].number)] = xy
            return inter
    
    def triple_crossing(self, objects):
        ans = {}
        inter = self.intersections(objects)
        for i in inter:
            temp = inter[i]
            for j in inter:
                if inter[j] == inter[i] and i != j and not(inter[j] in ans.values()):
                    ans[i+j[1:2]] = inter[j]
        return ans

    def get_info(self):
        print(self.vals)
        print(self.number)



line_1 = Solution()
line_2 = Solution()
line_3 = Solution()

lines = [line_2, line_3]
print(line_1.intersections(lines))

print(line_1.triple_crossing(lines))

line_4 = Solution()
line_5 = Solution()
line_6 = Solution()
line_7 = Solution()

lines = [line_5, line_6, line_7]

print(line_4.intersections(lines))
print(line_5.intersections([line_4, line_7, line_6]))
print(line_4.triple_crossing(lines))


