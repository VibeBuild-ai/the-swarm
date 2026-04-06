# Projekt-Backlog: Vertex AI Agent Army 🎖️

## 1. Basis-Setup (Lokal)
- [ ] Python Virtuelle Umgebung erstellen (`.venv`)
- [ ] Google ADK installieren (`pip install google-adk`)
- [ ] `agent.py` mit Basis-Logik (Uhrzeit-Tool) erstellen
- [ ] Lokalen Testlauf mit `adk web` durchführen

## 2. Google Cloud Integration
- [ ] `gcloud` Authentifizierung sicherstellen
- [ ] `.env` Datei mit Projekt-ID und Region anlegen
- [ ] Vertex AI API aktivieren

# 🚀 Operation "The Swarm" - YouTube Roadmap (Enterprise Edition)

## 🎥 Intro Hook (0:00 - 1:00)
- **Problem**: "KI-Agenten lokal auf dem Laptop laufen lassen ist cool, aber wer macht die Arbeit, wenn ihr schlaft?"
- **Lösung**: "Wir bauen heute 'Den Schwarm'. Ein System basierend auf Schwarmintelligenz, das nativ in der Google Cloud (Vertex AI) lebt."
- **Showcase**: Zeige das neue **ADK Swarm Control Dashboard** (index.html).

## 🛠 Teil 1: Der Code (1:00 - 5:00)
- Zeige kurz den `Commander` in `the_swarm/agent.py`.
- Erkläre die Delegation: "Der Commander befehligt den Swarm Researcher, den Swarm Auditor und den Analysten."
- **Code-Snippet**: `root_agent = Agent(sub_agents=[commander, researcher...])`

## ☁️ Teil 2: Google Cloud Go-Live (5:00 - 8:00)
- Terminal-Befehl zeigen: `adk deploy agent_engine the_swarm`
- Point: "Pure Schwarmintelligenz in der Cloud – ohne Wartungsaufwand."
- Zeige kurz die **Vertex AI Agent Engine Console**.

## 💎 Teil 3: Das Swarm Control Dashboard (8:00 - 12:00)
- Zeige die `index.html`.
- **Key-Message**: "Link zum Dashboard-Code in der Beschreibung. Hol dir deine eigene Schwarm-Kontrolle!"
- Zeige das **One-Click Deployment**: Klick auf `publish.bat`.

## 🏁 Outro (12:00+)
- "Dein Schwarm arbeitet, während du träumst. Bis zum nächsten Video!"
- Call to Action: "Abonnieren, GitHub-Link checken und den Schwarm starten!"

---

## 🛠 Spickzettel für dich (Commands):
- **Dashboard lokal ansehen**: Einfach `index.html` im Browser öffnen.
- **In die Cloud schieben**: 
  `adk deploy agent_engine the_army --project "DEIN_PROJEKT" --region "us-central1" --display_name "Die Armee"`
- **Live gehen**: `publish.bat` ausführen.

## 3. "The Army" - Multi-Agenten Logik
- [ ] Market Researcher Agent definieren (News/Trends)
- [ ] Code Auditor Agent definieren (Repo-Sim)
- [ ] Commander (Root Agent) zur Orchestrierung bauen

## 4. Deployment
- [ ] `agent.yaml` für Vertex AI Agent Engine erstellen
- [ ] Deployment-Befehl ausführen
- [ ] Monitoring im Google Cloud Dashboard prüfen
