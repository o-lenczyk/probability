# Definicje wyników i prawdopodobieństw dla 1. kolejki
from itertools import product

# Śląsk - Górnik
slask_probs = {
    "win": (0.27, 3),
    "draw": (0.26, 1),
    "lose": (1 - 0.27 - 0.26, 0),
}

# Zagłębie - Widzew
zagleb_probs = {
    "win": (0.44, 3),
    "draw": (0.27, 1),
    "lose": (1 - 0.44 - 0.27, 0),
}

# Obliczamy wszystkie możliwe scenariusze i ich prawdopodobieństwo
scenarios = []
for s_outcome, (s_prob, s_pts) in slask_probs.items():
    for z_outcome, (z_prob, z_pts) in zagleb_probs.items():
        combined_prob = s_prob * z_prob
        point_diff = s_pts - z_pts  # różnica punktów: Śląsk - Zagłębie
        scenarios.append({
            "slask_result": s_outcome,
            "zagleb_result": z_outcome,
            "slask_points": s_pts,
            "zagleb_points": z_pts,
            "point_difference": point_diff,
            "probability": combined_prob
        })

# Obliczamy wartość oczekiwaną różnicy punktów po tej kolejce
expected_point_diff = sum(s["point_difference"] * s["probability"] for s in scenarios)

scenarios, expected_point_diff
#print(scenarios)
#print(expected_point_diff)

# Druga kolejka
# Śląsk - Jagiellonia
slask2_probs = {
    "win": (0.10, 3),
    "draw": (0.30, 1),
    "lose": (1 - 0.10 - 0.30, 0),
}

# Zagłębie - Motor
zagleb2_probs = {
    "win": (0.20, 3),
    "draw": (0.30, 1),
    "lose": (1 - 0.20 - 0.30, 0),
}

# Teraz musimy uwzględnić drugą kolejkę dla każdej kombinacji z pierwszej
scenarios2 = []
for s1 in slask_probs.items():
    for z1 in zagleb_probs.items():
        p1 = s1[1][0] * z1[1][0]
        pts1_s = s1[1][1]
        pts1_z = z1[1][1]

        for s2 in slask2_probs.items():
            for z2 in zagleb2_probs.items():
                p2 = s2[1][0] * z2[1][0]
                pts2_s = s2[1][1]
                pts2_z = z2[1][1]

                total_prob = p1 * p2
                total_slask = pts1_s + pts2_s
                total_zaglebie = pts1_z + pts2_z
                diff = total_slask - total_zaglebie

                scenarios2.append({
                    "slask_points": total_slask,
                    "zagleb_points": total_zaglebie,
                    "point_difference": diff,
                    "probability": total_prob
                })

# Obliczamy wartość oczekiwaną różnicy punktów po dwóch kolejkach
expected_diff_2rounds = sum(s["point_difference"] * s["probability"] for s in scenarios2)

expected_diff_2rounds


#print(scenarios2)
#print(expected_diff_2rounds)

# Trzecia kolejka
# Śląsk - Puszcza
slask3_probs = {
    "win": (0.25, 3),
    "draw": (0.50, 1),
    "lose": (1 - 0.25 - 0.50, 0),
}

# Zagłębie - Cracovia
zagleb3_probs = {
    "win": (0.20, 3),
    "draw": (0.40, 1),
    "lose": (1 - 0.20 - 0.40, 0),
}

# Uwzględniamy 3. kolejkę dla każdego scenariusza z dwóch pierwszych
scenarios3 = []
for s2 in scenarios2:
    for s3 in slask3_probs.items():
        for z3 in zagleb3_probs.items():
            p3 = s3[1][0] * z3[1][0]
            pts3_s = s3[1][1]
            pts3_z = z3[1][1]

            total_prob = s2["probability"] * p3
            total_slask = s2["slask_points"] + pts3_s
            total_zaglebie = s2["zagleb_points"] + pts3_z
            diff = total_slask - total_zaglebie

            scenarios3.append({
                "slask_points": total_slask,
                "zagleb_points": total_zaglebie,
                "point_difference": diff,
                "probability": total_prob
            })

# Obliczamy wartość oczekiwaną różnicy punktów po trzech kolejkach
expected_diff_3rounds = sum(s["point_difference"] * s["probability"] for s in scenarios3)

expected_diff_3rounds
p=0
for a in scenarios3:
    if a['point_difference']>5:
        print (a['probability'])
        p+=a['probability']
print(p)
