n = int(input("enter no. of scores: "))
li=[]
for i in range(n):
    el=int(input("enter:"))
    li.append(el)
maximum=max(li)
li.remove(maximum)
runner_score=max(li)
print(runner_score)