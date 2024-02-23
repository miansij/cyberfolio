## certification BLOC 5: Projet Getaround
Nom : NSOKI MIANSI Ndangani

email : jcmiansi@gmail.com

vidéo de la présentation sur ce lien: https://share.vidyard.com/watch/uh8aJsxj9RD7q5AAvfQMWd?

lien du projet sur drive: https://drive.google.com/drive/folders/1gfv4Z_Uf3u1HGnT0PG3w_jfD-zoAopRW?usp=share_link

contenu: 1 notebook d'analyse: Projet Getaround delay analysis Ndangani.ipynb
	 
	 1 notebook de prédictions: Projet Getaround price_prediction Ndangani.ipynb

	 1 fichier main.py ,  fichier de notre API (local) sous FastAPI, pour l'ouvrir, étant dans le même repertoire, lancer un terminal et taper:
	 	uvicorn main:getaround --port 7000 . C'est l'API des prévisions.
	 	
	 1 fichier dashboard.py,  de déploiement sous streamlit (local). Pour le lancer, étant dans le même repertoire, lancer un terminal et taper:
	 	streamlit run dashboard.py --server.port 7001
	 
	 1 dossier src
	 
	 
Ce projet comporte 2 parties:
 	
 	1 partie analyse de situation: 
 		
 		présenter des chiffres pertinents qui permettront de comprendre et régler un problème de retard dans les check-outs.
 		quel délai après remise de véhicule faut-il prévoir pour une seconde location
 		quel en seront les impacts sur le chiffre d'affaire
 		
 		Ensuite déployer un dashboard pour montrer les indicateurs marquants et éventuellement quelques graphiques. Cela a été fait avec Streamlit.
 				       
 				       
 				       
 				  
	
	1 partie prédiction du prix de location quotidien d'une voiture sur un dataset de plus de 4000 lignes et 14 colonnes. 
	Il faut établir un modèle de prévision puis faire en sorte de pouvoir donner les prédictions du modèle en ligne à travers une API. 
	Pour cela j'ai utilisé FastAPI. J'ai créé plusieurs endpoints.
	 
	 
