## 🎳 Description du problème

Tu dois créer un programme qui, à partir d'une séquence valide de lancers pour une partie de bowling à 10 quilles
(version américaine), calcule le score total de la partie.

Contraintes :
- ✅ Pas besoin de vérifier la validité des lancers.
- ✅ Pas besoin de vérifier le nombre correct de lancers ou de frames.
- ✅ Pas besoin d’afficher les scores intermédiaires.

---

## 📏 Règles de calcul du score

- Une partie comprend 10 frames (tours).
- Dans chaque frame, le joueur a jusqu’à 2 lancers pour faire tomber les 10 quilles.
- Si les 10 quilles ne tombent pas en 2 lancers → score = total des quilles tombées.
- Si les 10 quilles tombent en 2 lancers → spare → score = 10 + nombre de quilles du lancer suivant.
- Si les 10 quilles tombent en 1 lancer → strike → score = 10 + total des 2 lancers suivants.
- Au 10e frame, si le joueur fait un spare ou un strike, il a droit à 1 ou 2 lancers bonus.
- Le score final est la somme des scores des 10 frames.

## 🧠 Astuce

Ce qui rend ce kata intéressant, c’est la gestion des bonus (lookahead) :

- Pour un spare, il faut attendre le lancer suivant.
- Pour un strike, il faut attendre les deux lancers suivants.

## 🧪 Cas de test suggérés

- X X X X X X X X X X X X	12 strikes	300
- 9- 9- 9- 9- 9- 9- 9- 9- 9- 9-	10 fois 9 + 0	90
- 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5	10 spares + 5	150
 
Légende :
X = strike, / = spare, - = raté (0 quille)
