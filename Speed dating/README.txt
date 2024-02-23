## certification BLOC 2: PROJET SPEED DATING

Nom : NSOKI MIANSI Ndangani

email : jcmiansi@gmail.com

vidéo de la présentation sur ce lien: https://share.vidyard.com/watch/d7MG4fWKBeTg7sJroYwBpJ?

lien du projet sur drive: https://drive.google.com/drive/folders/1eIp_fl2QPU9HLnuJ7O6VLYYCGAiDS44X?usp=share_link

			


contenu: 1 notebook, 

	 1 repertoire src


Le projet SPEED DATING est un projet de visualisation et d'exploration de données. 

Ces données ont été recueillies auprès de participants à des événements expérimentaux de speed dating entre 2002 et 2004. Au cours de ces événements, les participants avaient un "premier rendez-vous" de quatre minutes avec chaque autre participant du sexe opposé. À l'issue de ces quatre minutes, les participants devaient indiquer s'ils souhaitaient revoir leur partenaire. Il leur était également demandé d'évaluer leur partenaire sur six critères :

    Attractivité
    Sincérité
    Intelligence
    Amusement
    l'ambition
    Intérêts communs.

L'ensemble de données comprend également des données de questionnaire recueillies auprès des participants à différents moments du processus. Ces champs comprennent

    données démographiques
    les habitudes de rencontre
    la perception de soi à travers des attributs clés
    les croyances sur ce que les autres considèrent comme précieux chez un partenaire
    les informations sur le mode de vie


source: https://datahub.io/machine-learning/speed-dating#readme



L'objectif est d'essayer de comprendre ce qui se passe lors d'un speed dating et surtout de comprendre ce qui va influencer l'obtention d'un second rendez-vous.
Pour réussir ce projet, il nous est demandé de faire une analyse descriptive des principaux facteurs qui influencent l'obtention d'un second rendez-vous.
Pour plus de détail: [Speed Dating Dataset](https://www.kaggle.com/annavictoria/speed-dating-experiment#Speed%20Dating%20Data%20Key.doc)

1. INTRODUCTION
	C'est un projet dont le dataset comporte 195 colonnes et 8378 lignes, un très grand nombre de valeurs nulles, des outliers.
	La colonne 'num_in_3' a 92.03% de NaN plus d'une dizaine d'autres colonnes ont plus de 75% de NaN. 

	1) Pour retenir la signification des colonnes. J'ai donc créé des dictionnaires et fonctions pour à tout moment de connaître le sens d'une colonne.
	
	2) Pour connaître directement et en même temps les infos sur ses stats:
		nombre et pourcentage de valeurs nulles,
		indice de la colonne, 
		type, 
		nombre d'outliers supérieurs et inférieurs pour les données numériques, 
		le max et le min pour les données numériques sinon pour les données de type 'object' le mode et sa fréquence. 
	
	3) J'ai aussi regroupé les colonnes dans des listes selon une sémantique ou thème ou nature.

2. TRAITEMENT DES VALEURS NULLES ET DES VALEURS ABERRANTES:

	Traiter le grand nombre de valeurs nulles du dataset: Quelle stratégie adopter: supprimer ou imputer. 
	 
	En cas d'imputation, imputation par la moyenne,la médiane ou autre, KnnImputer ou la régression linéaire.
	Ce projet étant le premier du cursus, j'ai décidé de ne pas utiliser KnnImputer ou la régression linéaire pour l'imputation.
	En effet ce sont des connaissances qui sont supposées par encore apprises à ce stade du cursus.

	J'ai décidé de n'imputer que pour l'age et les revenus. Pour l'âge l'imputation s'est faite par la médiane.
	Pour le revenu, l'imputation s'est faite par les médianes des groupements de revenus par age. 
	J'ai choisi l'age parce que très peu de NaN et que parmi les éléments de la liste c'est celle qui avait la corrélation la moins faible avec le revenu.

	Et J'ai décidé aussi de ne traiter que les outliers de ces 2 colonnes.

	Il faut souligner que dans cet exercice, la présence de valeurs nulles et d'outliers n'est pas bloquant comme ce serait le cas en machine learning.
	En ML certains modèles ne fonctionnent pas s'il y a des valeurs nulles et les outliers ruineraient les prédicions.

3. EQUILIBRAGE DU DATASET FINAL, CORRELATIONS ET DECODAGE: 

	le dataset initial avait 50.06% d'hommes et 49.94% de femmes alors que le dataset final a 39.26% d'hommes et 60.74% de femmes. 
	J'ai donc en utilisé un échantillon aléatoire parmi les enregistrements des femmes pour avoir le même ratio homme/femme qu'au départ. 

	Ensuite, j'ai créé un dataframe de paires de colonnes et leurs correlations, trié par ordre décroissant sur la corrélation. 
	Ce travail pour avoir des indications éventuelles sur l'analyse à faire.

	Et enfin, j'ai décodé certaines colonnes, ce qui a eu pour effet d'en faire des colonnes de type object, facilitant la visualisation et l'analyse. 
	Ainsi donc je n'ai eu à utiliser yticks qu'une seule fois.

4. ANALYSE:

	La surreprésentation du type caucasien ne permet pas de tirer des conclusions générales sur l'importance de la race dans les choix. 
	Sinon on serait enclin à dire que les 'caucasiens' matchent plus dans leur propre race à l'inverse de toutes les autres communautés;
	et que l'importance d'être de la même race augmente en cas de matchs. 
	
	Autre chose de notable c'est des fortes variations chez les 'asian' de leur participation en cas de match': 
		Les femmes 'asian' augmentent leurs pourcentages de presque 6 points alors que les hommes 'asian' le baissent de + 4 points.
		
	Mais tout ceci est à prendre avec des pincettes à cause du déséquilibre dans la colonne 'race'.

	Globalement, la religion n'a pas grande influence pour la plupart des gens, hommes ou femmes. 
	Mais pour ceux qui lui accordent de l'importance (note > 6), les femmes sont plus présentes

	Pour les match, globalement, l'attirance, l'intelligence et le fun viennent en premier chez les femmes. Chez les hommes ils sont plutôt à égalité. 
	Mais au-delà d'une notation de 8, les hommes s'intéressent à l'attirance et les femmes s'intéressent largement plus aux autres attributs.

	Les femmes participent pour faire des rencontres et les hommes plutôt pour le fun.

	Ceux ont 2 RDV par mois font plus de match.
	
	Ceux qui sortent plusieurs fois par semaine font plus de match.

