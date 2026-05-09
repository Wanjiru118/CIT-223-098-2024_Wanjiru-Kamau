regions = ["WA","NT","SA","QLD","NSW"]
colors = ["Red","Green","Blue"]

neighbors = {
    "WA": ["NT","SA"],
    "NT": ["WA","SA","QLD"],
    "SA": ["WA","NT","QLD","NSW"],
    "QLD": ["NT","SA","NSW"],
    "NSW": ["SA","QLD"]
}

solution = {}

def valid(region, color):
    for n in neighbors[region]:
        if n in solution and solution[n] == color:
            return False
    return True

def backtrack(i=0):
    if i == len(regions):
        return True

    region = regions[i]

    for color in colors:
        if valid(region, color):
            solution[region] = color
            if backtrack(i+1):
                return True
            del solution[region]
    return False

backtrack()

print(solution)