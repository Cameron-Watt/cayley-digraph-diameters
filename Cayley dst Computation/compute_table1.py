import numpy as np
from cayley_digraphs import cyclic_cayley, get_orbits, cayley_times, get_H_sets
import time as tm

n = 7

best_dst_data = np.zeros((n,n,n))

best_dst_data[:] = np.nan

start_time = tm.time()

best_graphs = [[[[f"s={s}"] for s in range(n)] for _ in range(n)] for _ in range(n)]

Max = n

for t in range(1, Max):
    for s in range(t,Max):
        for H_size in range(t, Max):
            best_tsH_graphs = []
            
            best_diam = float('inf')
            
            H_sets = get_H_sets(n, H_size)

            for H_set in H_sets:
                H = H_set[0]
#                 print(H)
                g = cyclic_cayley(n, H)

                avg_speed, min_speed, max_speed, sync_probability, avg_step = cayley_times(g, t, s)
                
                if sync_probability == 1:
                    diam = 1/min_speed
                else:
                    diam = float('inf')
                    
                if diam < best_diam:
                    best_diam = diam
                    best_tsH_graphs = [H]
                elif diam == best_diam:
                    best_tsH_graphs.append(H)
                    
            best_dst_data[H_size][s][t] = best_diam
            
            if len(best_tsH_graphs) == len(H_sets):
                best_tsH_graphs = ["all graphs"]
            
            best_graphs[H_size][t][s].append(best_tsH_graphs)

for h in range(n):
    for t in range(n):
        best_graphs[h][t].insert(0,f"t={t}")
    best_graphs[h].insert(0,f"h={h}")

print("--- %s seconds ---" % (tm.time() - start_time))


# Prints the smallest dst diameters for each |H|, s, and t
# Rows are indexed by s and columns are indexed by t

print(f"n = {n}")
for i in range(1,Max):
    print(f"|H| = {i}")
    print(best_dst_data[i,1:Max,1:Max])