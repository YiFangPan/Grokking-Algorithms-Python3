

states_need_cover = set(["mt","wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = []

while states_need_cover:
    best_station = None
    states_covered = set()

    # find maximum number for cover states in stations
    for station_name, station_cover_states in stations.items():
        # & => Collection(Set) Intersection
        coverd = states_need_cover & station_cover_states
        if(len(coverd) > len(states_covered)):
            best_station = station_name
            states_covered = coverd
    
    # states_need_cover = states_need_cover - states_covered
    # - => Collection(Set) Difference
    # Remove this sation cover's states from states_need_cover 
    # Next loop do not need consider this sation cover's states 
    states_need_cover -= states_covered

    final_stations.append(best_station)

print(final_stations);
