# Betriebsdokumentation
[[_TOC_]]
## Einführungstext 

Script 1: ermöglicht es mehre Git Repos einfach zu klonen und pullen anhand von einer Datei.

Scipt 2: kann ein File erstellen mit den Commits von mehren Repos. Analysen können erstellt werden wie zum Beispiel wer wieviel gemacht hat.

## Installationsanleitung für Administratoren

### Installation
Wichtig: git und python3 müssen vorinstalliert werden

Dann muss das Repository geclont werden:
<pre>git clone https://github.com/juliGou/m122_projektarbeit_Albanese_Goudsmit.git</pre>

### Konfiguration

Im Konfigfile kann der Pfad für den Output des Commitlogs angegeben werden. Betrifft Skript 2.
<pre>[config]
LOG_DIR = '/home/linuxjg/logFiles/'</pre>

## Bediensanleitung Benutzer

- git clonen:
<pre>git clone https://github.com/juliGou/m122_projektarbeit_Albanese_Goudsmit.git</pre>

Skript 1
- csv anpassen
- Script ausführen: <pre>python3 git_clone_update_repos.py -b pfad/der/gitRepos/ -i csv/inputfilename.csv</pre>

Skript 2
- konfigfile anpassen
- Script ausführen: <pre>python3 git_extract_commits.py -b pfad/der/gitRepos/ -f outputfilename.csv</pre>


