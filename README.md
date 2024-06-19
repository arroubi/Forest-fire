# Forest-fire

read_config: Lecture du fichier de configuration JSON et retourne un dictionnaire contenant les paramètres.

initialize_grid: Initialisation de la grille avec les dimensions spécifiées et placement des feux initiaux aux positions indiquées.

display_grid: Affichage de la grille de la forêt.

spread_fire: Simulation de la propagation du feu d'une étape à l'autre selon la probabilité donnée. Les cases en feu deviennent des cendres et le feu peut se propager aux cases adjacentes.

is_fire_present: Vérifie si des cases en feu sont encore présentes dans la grille.

main: Gestion de la boucle principale de la simulation, affichant l'état de la grille à chaque étape jusqu'à ce que le feu s'éteigne complètement.
