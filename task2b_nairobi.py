subcounties = ["Westlands","Kasarani","Embakasi","Langata","Kibra"]
colors = ["Red","Green","Blue","Yellow"]

adj = {s: [] for s in subcounties}

for i in range(len(subcounties)-1):
    adj[subcounties[i]].append(subcounties[i+1])
    adj[subcounties[i+1]].append(subcounties[i])

solution = {}

for node in subcounties:
    for color in colors:
        if all(solution.get(n) != color for n in adj[node]):
            solution[node] = color
            break

print(solution)