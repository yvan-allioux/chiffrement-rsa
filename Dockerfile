# Utilise l'image Docker officielle pour Python 3.10.6
FROM python:3.10.6

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier rsa.py dans le conteneur
COPY rsa.py .

# Lance un shell Bash à l'exécution du conteneur
CMD ["/bin/bash"]

# COMMANDE

#docker build -t rsa_py .

#docker run -it rsa_py

#python rsa.py


