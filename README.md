# genererAttestation
Un script python pour générer l'attestation dérogatoire en utilisant selenium (Driver Firefox).

# Comment ça marche

1. Remplir le fichier `config.py` par vos informations personnelles et renseigner l'adresse mac de votre téléphone
2. sniffer le réseau pour détecter votre téléphone, si on le trouve pas cela veut dire que vous n'êtes pas chez vous !
3. remplir le formulaire automatiquement
4. envoyer le mail avec l'attestation en PJ sur votre gmail :)

**P.S : Le script marche que pour gmail !**

# Configuration

## Autoriser Google pour les applications moins sécurisées
Pour faire marcher le script (envoie du mail), faut se rendre au site de google dev : https://myaccount.google.com/lesssecureapps pour donner autorisation aux apps moins sécurisées, et désactiver l'authentification double facteur si c'est le cas pour votre compte google.

## Installer les packages python

Le premier pckage python pour sniffer le réseau et détecter votre smartphone, ce package depend de `python-nmap` :
```python
pip3 install who-is-on-my-wifi --upgrade
```

le deuxième package est necessaire pour récupérer les informations du réseau local
```python
pip3 install python-nmap
```

enfin, installer le dernier package pour l'automatisation du formulaire :
```python
pip3 install selenium
```

# Pour le lancer
pour lancer le script, il suffit :
```python
python main.py
```
