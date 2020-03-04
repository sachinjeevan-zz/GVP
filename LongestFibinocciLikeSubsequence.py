import collections
class CLFS:
    def __init__(self,x):
        self.x = x
        self.n = len(self.x)
        self.ans = collections.defaultdict(lambda:2)
        self.ind = {}
        for i,j in enumerate(self.x):
            self.ind[j]=i
        self.maxi,self.a,self.b=-1,-1,-1
    def solve(self):
        for k in range(2,self.n):
            for j in range(1,k):
                ele = self.x[k]-self.x[j]
                try:
                    i=self.ind[ele]
                except KeyError:
                    i=None
                if(i!=None and i<j):
                    self.ans[j,k]=self.ans[i,j]+1
                    if(self.ans[j,k]>self.maxi):
                        self.maxi=self.ans[j,k]
                        self.a,self.b=j,k
    def LFS(self,maxi,a,b):
        if(maxi>=0):
            self.LFS(maxi-1,b-a,a)
            print(a,end=" ")
if __name__=="__main__":
    print("I am the main file")
else:
    print("I am a module")