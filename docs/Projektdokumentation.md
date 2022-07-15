# Projekt Dokumentation

[[_TOC_]]

## Lösungsdesign
Anhand der Analyse wurde folgendes Lösungsdesign entworfen.

### Aufruf der Skripte

Script 1: <br>
Beim aufrufen des Skriptes, muss das File angegeben werden, wellches die Repos und dem Pfad wohin sie geklont werden sollen, enthält. 
<br>Beispiel: skript1.bash -b /home/user/repos -i repolist.csv

Skript 2: <br>
Diese Script wird mit 2 Parameters gestartet <Verzeichnis der Repos> und <Pfad des Files>. Zudem wird im Konfigfile der Pfad des outputfiles mitgegeben.
<br>Beispiel: skript1.bash -b /home/user/repos -f output.csv

### Ablauf der Automation
Skript 1: <br>
![image](https://user-images.githubusercontent.com/72258756/176767389-081461f0-8ecd-49e5-9a92-96883f4610c0.png)

Skript 2: <br>
![image](https://user-images.githubusercontent.com/72258756/176768280-9b2319c7-f0bc-43db-9ef3-d8ef4cb4b813.png)


### Konfigurationsdateien

Script 1: benötigt kein Konfigurationsdatei. Alle Konfigurationen für das Skript werden mit den Parameters beim Aufruf des Sktiptes mitgegeben.

Script 2: in der [Konfigurationsdatei](https://github.com/juliGou/m122_projektarbeit_Albanese_Goudsmit/master/etc/config.conf), wird der Pfad des Outputfiles angegeben.
  <pre>[config] 
LOG_DIR = '/home/linuxjg/logFiles/'
</pre>

