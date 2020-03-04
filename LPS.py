def LPS(dp,i,j,s,ans):
    if(dp[i][j]<0):
        return
    elif(dp[i][j]!=0):
         if(s[i]==s[j]):
            LPS(dp,i+1,j-1,s,ans+s[i])
            dp[i][j]*=-1
         else:
            if(dp[i][j-1]<0):
                if(dp[i][j-1]*-1<=dp[i+1][j]):
                    LPS(dp,i+1,j,s,ans)
            else:
                if(dp[i][j-1]>dp[i+1][j]):
                    LPS(dp,i,j-1,s,ans)
                    dp[i][j]*=-1
                elif(dp[i+1][j]>dp[i][j-1]):
                    LPS(dp,i+1,j,s,ans)
                    dp[i][j]*=-1
                else:
                    LPS(dp,i,j-1,s,ans)
                    LPS(dp,i+1,j,s,ans)
                    dp[i][j]*=-1

    else:
        if(dp[0][-1]%2==0):
            print(ans+ans[::-1])
        else:
            print(ans+ans[-2::-1])

s=input()
n=len(s)
dp = [[0]*n for i in range(n)]
for i in range(0,n):
    dp[i][i]=1
i,j,k=0,1,1
while(k!=n):
    i=0
    j=k
    while(j<n):
        if(s[i]==s[j]):
            dp[i][j]=dp[i+1][j-1]+2
        else:
            dp[i][j]=max(dp[i][j-1],dp[i+1][j])
        i+=1
        j+=1
    k+=1
for i in range(n):
    print(*dp[i])
i,j=0,n-1
ans=""
LPS(dp,i,j,s,ans)
for i in range(n):
    print(*dp[i])
'''
while(dp[i][j]!=0):
    if(s[i]==s[j]):
        ans=ans+s[i]
        i+=1
        j-=1
    else:
        if(dp[i][j-1]>=dp[i+1][j]):
            j-=1
        else:
            i+=1
if(dp[0][n-1]%2==0):
    print(ans+ans[::-1])
else:
    print(ans+ans[-2::-1])    
'''