Projet Bloc n°3 : projet Walmart Sales

Nom : NSOKI MIANSI Ndangani

email : jcmiansi@gmail.com

vidéo de la présentation sur ce lien: 

lien du projet sur drive: 

contenu: 1 notebook, 1 dossier src


Le projet Walmart Sales

Le projet Walmart Sales porte sur la prévision des ventes hebdomadaires du groupe Walmart.
La particularité est le dataset très léger (150 lignes).

I.  Analyse et préprocessing
    
    Il y a bien évidemment une analyse exploratoire des données qui nous a permis de constater:
    qu'il ny a pas de données invalides, un certain nombre de données nulles qu'on va tenter de transformer avec KNNImputer.
    

    A. Préprocessing pandas
        1) concerne la date. Il a fallu créer de nouvelles données à partir de la date (year, month, dayofweek, day),
        puis supprimer la date. Tout ceci favorisant le sparse matrix.

        2) Il a fallu supprimer les outliers.

        3) Etablir 2 matrices de corrélations, triées sur la target pour nous en servir plus tard, lors des différents tests et pouvoir comparer.

    B. Préprocessing avec sklearn
        
II. La prédiction

    Nous avons commencé par utiliser toutes les données pour la première prévision.
    Ensuite nous avons systématiquement réduit le nombre de variables en nous servant du resultat des correlations des variables avec la target (weekly_Sales).
    Et nous avons observé les résultats.

    Nous avons gardé le meilleur résultat pour ensuite utiliser Gridsearch avec Ridge et Lasso pour l'améliorer en terme d'overfitting.
    
    Pour faciliter le travail nous avons écrit des fonctions qui nous permettaient de tester les divers cas.

