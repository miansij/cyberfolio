Projet Bloc n°1 : projet Uber pickups

Nom : NSOKI MIANSI Ndangani

email : jcmiansi@gmail.com

vidéo de la présentation sur ce lien: 

lien du projet sur drive: 
contenu: 1 notebook, 1 dossier src


Projet de machine learning non supervisé.

Il s'agit à partir des fichiers contenant les cordonnées des points de récupération des clients par les chauffeurs Uber,
de pouvoir déterminer les hot zones, c'est à dire les zones avec le plus d'activité.

Ensuite il s'agit de faire des recommandations de ces hot zones pour que réduire le temps d'attente des clients et optimiser les courses.

Dans un premier temps, il a fallu comparer Kmeans avec DBSCAN par rapport aux clusters. Kmeans donne des clusters de taille plus équivalentes et un meilleure découpage, il a donc été préférable de l'utiliser pour la suite.

Le dataset comporte huit fichiers dont 2 présentant un schéma différent et inexploitable car impossible de les merger avec les 6 autres.

Un grand nombre de données, au-delà du million, ce qui a conduit à utiliser des samples et une approche progressive.

Au départ, on a analysé quel est le mois présentant le plus d'activité, le jour, le jour de semaine et l'heure de plus grandes activités.
Et donc la baseline a été d'examiner une seule heure du mois de septembre pour faire le choix entre Kmeans et DBSCAN.

Ensuite seulement, nous avons fait l'analyse sur tout le mois de septembre avec Kmeans. La recommendation porte sur la présentation des zones les plus fréquentées 

pour un mois donné (en l'occurence septembre) et un jour de semaine donné et avec la possibilité de regarder l'activité aux différentes heures de la journée.
