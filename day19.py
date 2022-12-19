import re

data = [list(map(int, re.findall("\d+", i))) for i in open("testdata19.txt", "r").read().split("\n")]

# Format: id, ore (ore), clay (ore), obs (ore), obs (clay), geode (ore), geode (obs)

def bruteForce(blueprint, robots, resources, time):
    # Robots and resources are 4 long arrays. [ore, clay, obs, geode]

    if time == 0:
        return resources[3]
    
    # Collect resouces
    for i in range(4):
        resources[i] += robots[i]

    # No change
    geodes = bruteForce(blueprint, robots[::], resources[::], time - 1)

    # Make ore
    if resources[0] - robots[0] >= blueprint[1]:
        r = robots[::]
        r[0] += 1

        s = resources[::]
        s[0] -= blueprint[1]

        geodes = max(geodes, bruteForce(blueprint, r, s, time - 1))
    
    # Make clay
    if resources[0] - robots[0] >= blueprint[2]:
        r = robots[::]
        r[1] += 1

        s = resources[::]
        s[1] -= blueprint[2]

        geodes = max(geodes, bruteForce(blueprint, r, s, time - 1))
    
    # Make obs
    if resources[0] - robots[0] >= blueprint[3] and resources[2] - robots[2] >= blueprint[4]:
        r = robots[::]
        r[2] += 1

        s = resources[::]
        s[0] -= blueprint[3]
        s[1] -= blueprint[4]

        geodes = max(geodes, bruteForce(blueprint, r, s, time - 1))

    # Make geode
    if resources[0] - robots[0] >= blueprint[5] and resources[3] - robots[3] >= blueprint[6]:
        r = robots[::]
        r[3] += 1

        s = resources[::]
        s[0] -= blueprint[5]
        s[3] -= blueprint[6]

        geodes = max(geodes, bruteForce(blueprint, r, s, time - 1))

    return geodes

def efficientSimulate(blueprint):
    robots = [1, 0, 0, 0]
    resources = [0, 0, 0, 0]

    for t in range(30):
        # Collect resouces
        for i in range(4):
            resources[i] += robots[i]
        
        # Make geode bot if possible
        if resources[0] - robots[0] >= blueprint[5] and resources[3] - robots[3] >= blueprint[6]:
            robots[3] += 1
            resources[0] -= blueprint[5]
            resources[1] -= blueprint[6]
            continue
        
        # Determine what is limiting geode production
        rescpy = resources[::]
        while not (rescpy[0] - robots[0] >= blueprint[5] and rescpy[3] - robots[3] >= blueprint[6]):
            for i in range(4):
                rescpy[i] += robots[i]
        
        # Limited by ore
        if rescpy[3] - robots[3] >= blueprint[6]:
            # Build ore bot if possible
            if resources[0] - robots[0] >= blueprint[1]:
                robots[0] += 1
                resources[0] -= blueprint[1]
            
            continue
        # Limited by obsidian
        else:
            # Build obsidian bot if possible
            if resources[0] - robots[0] >= blueprint[3] and resources[2] - robots[2] >= blueprint[4]:
                robots[2] += 1
                resources[0] -= blueprint[3]
                resources[1] -= blueprint[4]
                continue
                
            # Find out what is limiting obsidian
            rescpy1 = resources[::]
            while not (rescpy1[0] - robots[0] >= blueprint[3] and rescpy1[2] - robots[2] >= blueprint[4]):
                for i in range(4):
                    rescpy1[i] += robots[i]
            
            # Limited by ore
            if rescpy1[2] - robots[2] >= blueprint[4]:
                # Build ore bot if possible
                if resources[0] - robots[0] >= blueprint[1]:
                    robots[0] += 1
                    resources[0] -= blueprint[1]
                
                continue
            # Limited by clay
            else:
                # Build clay bot if possible
                if resources[0] - robots[0] >= blueprint[2]:
                    robots[1] += 1
                    resources[0] -= blueprint[2]
                
                    continue

                # Maybe build ore bot. Could also be that it is caught otherwhere
    
    return resources[3]




# Iterate each blueprint
sum = 0

for i, x in enumerate(data):
    sum += (i + 1) * efficientSimulate(x)

print(sum)