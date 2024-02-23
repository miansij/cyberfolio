Projet Bloc n°4 : Projet AT&T spam detector

Nom : NSOKI MIANSI Ndangani

email : jcmiansi@gmail.com

vidéo de la présentation sur ce lien: https://share.vidyard.com/watch/UHVzbp5Wov67KYCQumRehu?

lien du projet sur drive: https://drive.google.com/drive/folders/1AeW3IBe0vx1mzChqcOjf6228y9sUWgxa?usp=share_link

contenu: 1 notebook, 1 dossier src


J'ai utilisé les contributions de VictorSanh et kamalkraj:
https://github.com/huggingface/transformers/blob/main/examples/research_projects/distillation/README.md
https://colab.research.google.com/github/peterbayerle/huggingface_notebook/blob/main/distilbert_tf.ipynb



I.Périmètres du projet

Dans ce projet il nous est demandé:

	de construire un détecteur de spam capable de détecter automatiquement les spams reçus par sms en se basant sur leur contenu.
	
	Il est conseillé d'utiliser un modèle de deep learning simple pour faire du transfert learning. 
	
	Il faut donc trouver un modèle existant et l'adapter pour qu'il soit capable de détecter les spams.
	
	C'est un problème d'analyse sémantique, d'analyse des mots et de classification de texte.
	
	Pour ma part: 
		j'ai fait de l'EDA pour comprendre le dataset avec quelques visualisations. le dataset comprend 5572 lignes.
	
		j'ai fait du préprocessing textuel pour préparer les données, préprocessing particulier puisqu'il s'agit de travailler sur du texte,
		en le nettoyant de certains caractères (stop-words et tags html), enlever la ponctuation et mettre tout le texte en caractères minuscules.
		j'ai donc eu recours à de la lemmatisation et de la tokenisation.
		
		J'ai utilisé wordcloud pour visualiser les mots présents dans les spams et ceux pour les hams dans le dataset.  
		
		j'ai ensuite encodé le texte avec TfidfVectorizer et fait enduite du préprocessing traditionnel de machine learning (train set, test set).
		
		J'ai ensuite testé plusieurs modèles de machine learning et comparé leur résultat grâce à 'classification_report'. 
		Ces modèles sont du meilleur au moins bon dans le cas présent:
			
			SVM
			multinomialNB
			LogisticRegression
			ComplementNB
			
			
		Ensuite j'ai recherché un modèle préexistant de deep learning qui pouvait faire ce travail de prédiction de spams.
		Dans mes lectures je suis tombé sur DistilBert. C'est un modèle allégé et plus rapide de BERT et plus facile a utiliser.
		J'ai consulté le repo de VictorSanh avec comme contributeur kamalkraj:
					https://github.com/huggingface/transformers/blob/main/examples/research_projects/distillation/README.md

		J'ai finalement profité de leur code sur colab: 
					https://colab.research.google.com/github/peterbayerle/huggingface_notebook/blob/main/distilbert_tf.ipynb
		
		un modèle qui peut faire beaucoup de tâches comme expliqué ici:	https://paperswithcode.com/method/distillbert
		
		
		J'ai donc fourni mes données au modèle et juste adapté quelques noms de variables pour la prédicion. 
		J'ai aussi réduit les epoch à 1 parce c'est long. Mais au final le résultat est quand même meilleur que celui des modèles que j'ai utilisés.
			

