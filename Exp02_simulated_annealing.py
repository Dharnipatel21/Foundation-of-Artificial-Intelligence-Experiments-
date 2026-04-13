#2 local search alg.
import random, math
cities = {
    "New York": (40.7128, -74.0060), "London": (51.5074, -0.1278),
    "Dubai": (25.2048, 55.2708), "Tokyo": (35.6762, 139.6503),
    "Sydney": (-33.8688, 151.2093), "Paris": (48.8566, 2.3522),
    "Singapore": (1.3521, 103.8198), "Mumbai": (19.0760, 72.8777),
    "Chennai": (13.0827, 80.2707), "Berlin": (52.5200, 13.4050),
    "Toronto": (43.6510, -79.3470), "Beijing": (39.9042, 116.4074)
}
def haversine(c1, c2):
    lat1, lon1, lat2, lon2 = map(math.radians, [c1[0], c1[1], c2[0], c2[1]])
    a = math.sin((lat2-lat1)/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin((lon2-lon1)/2)**2
    return 6371 * 2 * math.asin(math.sqrt(a))
def total_dist(route):
    return sum(haversine(cities[route[i]], cities[route[(i+1)%len(route)]]) for i in range(len(route)))
def simulated_annealing(route, temp=10000, cooling=0.995):
    best = route[:]
    for _ in range(10000):
        i, j = sorted(random.sample(range(len(route)), 2))
        neighbor = route[:i] + route[i:j+1][::-1] + route[j+1:]
        if total_dist(neighbor) < total_dist(route) or random.random() < math.exp(-(total_dist(neighbor)-total_dist(route))/temp
            route = neighbor
        if total_dist(route) < total_dist(best): best = route
        temp *= cooling
    return best
def optimize_for_cities(selected_cities):
    missing = [c for c in selected_cities if c not in cities]
    if missing:
        print(f" Cities not found: {missing}")
        print(f" Available cities: {list(cities.keys())}")
        return
    optimized = simulated_annealing(selected_cities[:])
    print(f"\n Initial Distance : {total_dist(selected_cities):,.2f} km")
    print(f" Optimized Distance: {total_dist(optimized):,.2f} km")
    print(f" Saved             : {total_dist(selected_cities) - total_dist(optimized):,.2f} km\n")
    for i, city in enumerate(optimized):
        next_city = optimized[(i+1)%len(optimized)]
        print(f"   {city}  → {next_city} ({haversine(cities[city], cities[next_city]):,.1f} km)")
