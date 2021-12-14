# Assistant vocal

Petit test d'un assistant vocal avec un micro d'une qualité globalement nul.

## Installation

pip install -r requirements.txt

Télécharger : https://drive.google.com/file/d/0Bw_EqP-hnaFNN2FlQ21RdnVZSVE/view?resourcekey=0-CEkuW10BcLuDdDnKDbzO4w

SR_LIB=$(python -c "import speech_recognition as sr, os.path as p; print(p.dirname(sr.__file__))")
sudo apt-get install --yes unzip
sudo unzip -o fr-FR.zip -d "$SR_LIB"
sudo chmod --recursive a+r "$SR_LIB/fr-FR/"
