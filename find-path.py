
ways = {}
def find_shortest_way(planets):
    for i in planets:
        for j in planets:
            if i.id != j.id:
                minimum = i.planet.distance_to(j.planet)
                if i.planet.distance_to(j.planet) < minimum:
                    minimum = i.planet.distance_to(j.planet)
                    ways[i.id] = j.id
                else:
                    ways[i.id] = j.id
                    
    print(ways)

lines = []
def draw_ways(planets):
    for key in ways:
        for i in planets:
            if key == i.id:
                for j in planets:
                    if ways[key] == j.id:
                        line = play.new_line(color=i.planet.color, x=i.planet.x, y=i.planet.y,thickness=1, x1=j.planet.x, y1=j.planet.y)
                        lines.append(line)