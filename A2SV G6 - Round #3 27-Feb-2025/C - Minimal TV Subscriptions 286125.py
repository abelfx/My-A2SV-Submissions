# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import Counter
t = int(input())  

for _ in range(t):
    n, k, d = map(int, input().split()) 
    arr = list(map(int, input().split()))  
    window = Counter(arr[:d])  
    ans = len(window)  
    
    for i in range(d, n): 
        window[arr[i]] += 1  
        window[arr[i - d]] -= 1  
        
        if window[arr[i - d]] == 0:  
            del window[arr[i - d]]
        
        ans = min(ans, len(window))  
    
    print(ans)  


         