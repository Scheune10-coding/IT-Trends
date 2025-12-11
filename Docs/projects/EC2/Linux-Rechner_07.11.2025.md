## Linux-Rechner starten & einloggen (cal ausführen)

1. EC2 → Neue Instanz starten (Ubuntu oder Amazon Linux)
- .pem Datei zuweisen

2. Sicherheitsgruppe anpassen:
   - SSH (22) → eigene IP erlauben

3. Auf Instanz verbinden:
   ssh -i key.pem ec2-user@<PUBLIC-IP> (Amazon Linux)
   oder:
   ssh -i key.pem ubuntu@<PUBLIC-IP> (Ubuntu)
   
4. Befehl ausführen:
   cal