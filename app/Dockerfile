# Partir de l’image officielle de Python 3.7
FROM python:3.7-slim

# L'application va écouter sur le port 3000
EXPOSE ${PORT}

# Mettre le code de l’application dans le répertoire / de l’image
WORKDIR /

# Copier les librairie nécessaire à votre application
ADD requirements.txt /

# Installer les packages Python nécessaires dans requirements.txt
RUN pip install -r requirements.txt

# Copier le code de l’application dans le répertoire /
ADD . /

# Rendre exécutable le script pour attendre que la db se lance
RUN chmod +x /wait-for-it.sh

# Attendre que la db se lance sans timeout puis lancer le script app.py quand le container démarre
CMD /wait-for-it.sh database:3306 -t 0 && python -u app.py