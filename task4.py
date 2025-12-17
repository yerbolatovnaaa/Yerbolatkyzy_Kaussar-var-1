items = input().split()

if not items:
    print("")
else:
    result = [items[0]]
    
    for i in range(1, len(items)):
    
        if items[i] != items[i-1]:
            result.append(items[i])
            
    print(" ".join(result))