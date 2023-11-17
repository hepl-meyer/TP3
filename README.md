# TP3
Al’aide du logiciel Thonny ( ou VScode ou votre ide préféré ) , 
vous prendrez en main les librairies TCP-UDP(socket ), 
l'environnement Node-red et le système Git.
Grâce à votre programme , la carte esp8266 et votre ordinateur agiront de la façon suivante :
La carte se connecte à un point d’accès wifi ( ‘electroProjectWifi’ , ou autre réseau que vous maitrisez )
Lorsque la carte est connectée au réseau wifi , 
la carte allume une led pour indiquer que le dispositif est prêt à envoyer des données.
Votre ordinateur dispose d’un dashboard Node-red configuré de la façon suivante :
Uninput nodeTCP→Ungraphe(linechart ) affichant les nombres reçus
Uninput nodeUDP→Ungraphe(linechart) affichant les nombres reçus
La carte envoie régulièrement et rapidement ( testez plusieurs fréquences d’envoi ) 
des données à votre ordinateur( un nombre qui s’incrémente à chaque envoi ) 
sur une socket TCP ( librairie socket ) et simultanément sur une socket UDP.
L’ordinateur réceptionne ces données sur les deux inputs node ( Node-red ).
Comparer les données reçues.