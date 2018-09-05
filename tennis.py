def quicksort(g,p,r,players):
    if r-p<1:
        return ()
    if p<r:
        q=partition(g,p,r,players)
        quicksort(g,p,q-1,players)
        quicksort(g,q+1,r,players)
        
    return g
        
def partition(g,p,r,players):
    x=g[r]
    i=p-1
    j=p
    for j in range(p,r):
        m=players[g[j]]
        try:
            n=players[x]
            k=checkset(m,n)
        except IndexError:
            pass
        if(k):  
            i+=1
            temp=g[i]
            g[i]=g[j]
            g[j]=temp
    temp=g[i+1]
    g[i+1]=x
    g[r]=temp
    return i+1
                

def checkset(m,n):
    i=0
    while(i<6):
        if(i<4):
            if(m[i]==n[i]):
                i+=1
            elif(m[i]>n[i]):
                return False
                
            elif(m[i]<n[i]):
                return True
                
        else:
            if(m[i]>n[i]):
                return True
            elif(m[i]<n[i]):
                return False
            elif(m[i]==n[i]):
                i+=1
                
def rank(players):

    k=players.keys()
    g=list(k)
    g=quicksort(g,0,len(g)-1,players)
    k=len(g)-1
    for k in range(len(g)-1,-1,-1):
        str1=' '.join(str(e)for e in players[g[k]])
        print(g[k],str1)
        
        
        

event=[]
while 1:
    s=input()
    if(len(s)>0):
        event.append(s.strip())
    else:
        break
    
    
players={}                                            

for i in range(len(event)):
    k=event[i].find(":")
    winner=event[i][:k]
    wisplayed=winner in players.keys()
    s=event[i][k+1:]
    k=s.find(":")
    loser=s[:k]
    lisplayed= loser in players.keys()
    game=s[k+1:]
    game=game.split(",")
    setof5=len(game)<=5 and len(game)>3
    setof3=len(game)<=3
    if(not(wisplayed)):
        players[winner]=[]
        if(setof5):
            players[winner].append(1)
            players[winner].append(0)
            for v in range(4):
                players[winner].append(0)
        if(setof3):
            players[winner].append(0)
            players[winner].append(1)
            for v in range(4):
                players[winner].append(0)
                    
    else:
        if(setof5):
            players[winner][0]+=1
        if(setof3):
            players[winner][1]+=1
    if(not(lisplayed)):
        players[loser]=[]
        for v in range(6):
            players[loser].append(0)
        
    for x in range(len(game)):
         g=game[x].split("-")
         b=int(g[0])-int(g[1])
         if(b>=1):
             players[winner][2]+=1
             players[loser][4]+=1
             
         else:
            players[loser][2]+=1
            players[winner][4]+=1
        
         players[winner][3]+=int(g[0])
         players[winner][5]+=int(g[1])
         players[loser][3]+=int(g[1])
         players[loser][5]+=int(g[0])
             
rank(players)




        
        
            
        
        
    
                
    
    
    