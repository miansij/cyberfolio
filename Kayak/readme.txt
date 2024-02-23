Projet Bloc n°1 : projet Kayak

Nom : NSOKI MIANSI Ndangani

email : jcmiansi@gmail.com

vidéo de la présentation sur ce lien: https://share.vidyard.com/watch/vyhFhXYrrx1SNUpofijCzM?

lien du projet sur drive: https://drive.google.com/drive/folders/1lwUCfH1i77Vw58zrSjU0Z24LJOVAm2pN?usp=share_link

contenu: 1 notebook, 1 fichier python de scraping, 1 dossier images et 1 dossier src, 1 dasboard streamlit (facultatif) en local

Vous trouverez dans le dossier images:
1)les copies d'écran des cartes produites: 5 meilleures destinations et 20 meilleurs hôtels par destination (zoom sur une destination pour bien voir les 20 hôtels)
2) les preuves de création du bucket S3 et du fichier de sauvegarde sur amazon et de la base de données sur RDS et de la création des tables (vue sur mon pgAdmin)



I.Périmètres du projet

Dans ce projet il nous est demandé:

    A. à partir d'une liste de 35 villes de produire :
        1) une visualisation des 5 meilleures destinations touristiques
        2) une visualisation des 20 meilleurs hôtels aux alentours de chacune des 5 meilleures destinations

    B. pour des raisons de disponibilité des données pour les autres équipes et pour un éventuel déploiement:
        1) de stocker le fichier csv des données enrichies des villes et des hotels aux alentours dans un datalake (bucket Amazon S3) 
        2) A partir de ce bucket d'organiser ces données dans un datawarehouse (Amazon RDS) à partir duquel on pourra fournir les visualisations demandées.


II. Critères

    A. Les meilleures destinations touristiques
        Elles sont déterminées par les conditions climatiques uniquement. J'ai considéré 2 périodes dans l'année.
        Les critères que j'ai choisis sont purement subjectifs et ne dépendent que de moi pour corser un peu le sujet.
        Ces critères sont:
                        . apparent_temperature_max,
                        . apparent_temperature_min,
                        . rain_sum','snowfall_sum,
                        . windspeed_10m_max
        
        1) sunny_period
            Elle sétend du 01 mars au 31 octobre, les gens cherchent des conditions de soleil et de chaleur.
            Les meilleures destinations dans cette période sont celles où il y a le plus de chaleur.
            D'autres sous-critères s'ajoutent pour départager les meilleures destinations.

            by: ['dates','apparent_temperature_max','apparent_temperature_min','rain_sum','snowfall_sum','windspeed_10m_max']
            ascending: [True,False,False,True,True,True]

        2) snow_period
            Elle s'étend du 01 novembre au 28 février, les gens veulent de la neige.
            Les meilleures destinations dans cette période sont celles où il y a le plus de neige.
            D'autres sous-critères s'ajoutent pour départager les meilleures destinations.
            Dommage pour l'étude, il y a de moins en moins de neige en France, du-moins dans les villes retenues.
            
            by: ['dates','snowfall_sum','apparent_temperature_max','apparent_temperature_min','rain_sum','windspeed_10m_max']
            ascending: [True,False,False,True,True,True]
            
    B. Les meilleures hôtels
        Ils sont déterminés par le score donnés par les utilisateurs.
        Ici encore c'est un choix personnel, sachant que j'aurai pu conserver l'ordre renvoyé par le scraping et qui est déjà l'odre voulu par Booking.

III. DATA 

    A. pour les hotels
        les données sur les hôtels sont obtenues par scraping du site booking.com
        la ville,
        le nom de l'hôtel, 
        son Url sur la page de booking.com, 
        la distance du centre ville, 
        l'adresse, 
        la latitude et la longitude,
        le score donné par les usagers, 
        la description de l'hôtel.
        

    B. pour les destinations
        les données sont obtenues en exploitant les API de open-meteo,

        1) d'abord pour la localisation des villes
            . latitude
            . longitude

        2) Ensuite pour la météo, à partir de ces latitudes et longitudes, obtention des données suivantes
            . apparent_temperature_max,
            . apparent_temperature_min,
            . rain_sum','snowfall_sum,
            . windspeed_10m_max,
            . dates

IV. Analyse des données

    A. forme des données
        Il y a 2 formes de présentation des données dans les colonnes:
        
        1) sous forme de liste
            Toutes les données météo: listes de 7 éléments
        2) sous forme d'élément unitaire pour tout le reste
            mais attention: les les coordonnées issues du scraping de booking.com: string de 2 latitudes et 2 longitudes
            

    B. type des données

        1) les données issues du scraping sont toutes de type string
        2) les données issues des API sont de type float pour les latitudes, longitudes et pour le reste de type string

    C. Absence de donnés

        Le score des hôtels présentaient quelques valeurs nulles (4%)

V. Preprocessing

    A. changement de type

        1) coordinates de booking
            créer une liste avec 'split(',') puis changer le type de chaque élément de la liste en float ce qui sera utile poour la suite.
        2) score de booking
            donné sous forme française, avec la virgule. Donc d'abord transormer la virgule en point puis changer le type de string à float.
    
    B. Traitement des valeurs manquantes

        Concerne le score. Utilisation de KNNImputer qui semble plus judicieux que d'utiliser la moyenne.

    C. Feature engineering
        
        Plutôt que d'avoir 2 latitudes (nord-sud) et 2 longitudes (est-ouest), j'ai choisi d'avoir une latitude et une longitude.
        Comme le type de ces données a déjà été transformé en float, une simple moyenne permet cela.
    
    D. transformation des listes en valeurs unitaires

        A l'aide de la fonction 'weather_func_unpacked' sur le dataframe météo

 
