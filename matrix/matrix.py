from math import *

def clip(a, n, m):
    ans = []
    for i in range(0, len(a)):
        if i != n:
            temp = []
            for j in range(0, len(a[i])):
                if j != m:
                    temp.append(a[i][j])
                else:
                    pass
            ans.append(temp)
        else:
            pass
    return ans


class Matrix:
    
    file = open("matrix.txt", 'r')

    def __init__(self):
        self.vals = []
        temp = self.file.readline()
        while(temp.split() != []):
            self.vals.append(temp.split())
            temp=self.file.readline()
        for i in self.vals:
            for j in range(0, len(i)):
                i[j] = float(i[j])

    def get_values(self):
        return self.vals
    
    def print_values(self):
        for i in range(0, len(self.vals)):
            print(*self.vals[i])
        print()

    def __add__(self, other):
        if (len(self.vals) != len(other.vals)) or (len(self.vals[0]) != len(other.vals[0])):
            return -1
        else:
            ans = []
            for i in range(0, len(self.vals)):
                temp = []
                for j in range(0, len(self.vals[i])):
                    temp.append(self.vals[i][j] + other.vals[i][j])
                ans.append(temp)
            return ans

    def __mul__(self, other):
        ans = []
            
        if len(self.vals[0]) == len(other.vals):
            for k in range(0, len(self.vals)):
                arr_temp = []
                for i in range(0, len(self.vals)):
                    temp = 0
                    for j in range(0, len(self.vals[i])):
                        temp += self.vals[k][j] * other.vals[j][i]
                    arr_temp.append(temp)
                ans.append(arr_temp)
            return ans 
        else:
            return -1
     
    def multiplicate(self, a):
        for i in range(0, len(self.vals)):
            for j in range(0, len(self.vals[i])):
                self.vals[i][j] *= a
        return self        

    def trans(self):
        ans = []
        for i in range(0, len(self.vals[0])):
            ans.append([])
            for j in range(0, len(self.vals)):
                ans[i].append(self.vals[j][i])
        self.vals = ans
        return self
    
    def det(self, m):
        if len(m) != len(m[0]):
            return "ERR"
        elif len(m) == 2:
            return m[0][0]*m[1][1] - m[0][1]*m[1][0]
        else:
            det = 0
            for i in range(0, len(m[0])):
                det += (-1)**(i) * m[0][i] * self.det(clip(m, 0, i))
            return det
    def write_matrix(self, name):
        f = open(name, 'w')
        for i in range(0, len(self.vals)):
            for j in range(0, len(self.vals[i])):
                f.write(str(self.vals[i][j]) + " ")
            f.write("\n")
        f.close()


m1 = Matrix()
m2 = Matrix()

m2.trans().print_values()
print(m1.det(m1.get_values()))
m2.write_matrix('asdasd.txt')
