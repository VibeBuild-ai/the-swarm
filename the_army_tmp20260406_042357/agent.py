from google.adk import Agent
import datetime
import os

# --- TOOLS ---

def get_current_time() -> str:
    """Gibt die aktuelle Zeit und das Datum zurück."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_to_desktop(filename: str, content: str) -> str:
    """Erstellt eine Textdatei mit dem angegebenen Inhalt direkt auf dem Desktop des Nutzers."""
    try:
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        file_path = os.path.join(desktop_path, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Erfolgreich! Die Datei '{filename}' wurde auf deinem Desktop gespeichert."
    except Exception as e:
        return f"Fehler beim Speichern: {str(e)}"

def search_market_data(topic: str) -> str:
    """Scannt Markt-Daten und aktuelle News für den Bericht (Simuliert)."""
    return (f"ANALYSE-ERGEBNIS ({get_current_time()}): Der Bereich '{topic}' zeigt ein "
            "Wachstum von 22%. Besonders gefragt sind integrierte Multi-Agenten-Lösungen.")

def check_code_standards(repo_path: str) -> str:
    """Führt einen Sicherheits- und Compliance-Check für den Code durch (Simuliert)."""
    return (f"CODE-AUDIT FÜR '{repo_path}': Alle Sicherheits-Checks bestanden. "
            "Optimierung: Pydantic v2 Migration empfohlen für 15% Performance-Boost.")

# --- THE ARMY (Sub-Agents) ---

# 1. Market Researcher
market_researcher = Agent(
    name="market_researcher",
    description="Analysiert Märkte, Trends und Wettbewerber.",
    model="gemini-2.5-flash",
    instruction="""
    Du bist ein Experte für Marktanalyse. Nutze 'search_market_data', um Informationen zu sammeln.
    Deine Berichte müssen präzise und für Entscheidungsträger optimiert sein.
    """,
    tools=[search_market_data]
)

# 2. Code Auditor
code_auditor = Agent(
    name="code_auditor",
    description="Spezialist für Software-Qualität und Sicherheit.",
    model="gemini-2.5-flash",
    instruction="""
    Du prüfst Code auf Standards. Nutze 'check_code_standards'.
    Gib konstruktives Feedback und klare Handlungsempfehlungen.
    """,
    tools=[check_code_standards]
)

# 3. Personal Analyst
personal_analyst = Agent(
    name="personal_analyst",
    description="Erstellt finale Briefings und liefert sie an den Nutzer aus.",
    model="gemini-2.5-flash",
    instruction="""
    Du strukturierst das Wissen der anderen Agenten. 
    Verwende 'save_to_desktop', um das Endergebnis als Datei zu liefern.
    Nutze 'get_current_time', um sicherzustellen, dass jedes Briefing aktuell ist.
    """,
    tools=[save_to_desktop, get_current_time]
)

# --- COMMANDER (Root Agent / Orchestrator) ---

root_agent = Agent(
    name="commander",
    description="Der strategische Kopf von 'The Army'. Koordiniert Researcher, Auditor und Analyst.",
    model="gemini-2.5-flash",
    instruction="""
    Du bist der Commander. Wenn der Nutzer eine Mission startet:
    1. Beauftrage den 'market_researcher' mit der Untersuchung.
    2. Beauftrage den 'code_auditor' mit der technischen Prüfung.
    3. Gib alle Ergebnisse an den 'personal_analyst' weiter, damit dieser das finale Briefing auf den Desktop schreibt.
    Führe den Nutzer freundlich durch den Prozess.
    """,
    sub_agents=[market_researcher, code_auditor, personal_analyst]
)
