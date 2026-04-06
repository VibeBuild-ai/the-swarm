import os
from google.adk import Agent, AgentEngine

# --------------------------------------------------------------------------------
# VIBE BUILD | THE SWARM (ALPHABET ADK SHOWCASE)
# --------------------------------------------------------------------------------
# This system uses the Google Multi-Agent Orchestration Engine (ADK)
# to orchestrate a hierarchical expert swarm for Market Analysis & Security.
# --------------------------------------------------------------------------------

def save_to_desktop(filename: str, content: str) -> str:
    """Uses the ADK Tool Engine to secure highly sensitive reports locally."""
    from pathlib import Path
    desktop = Path.home() / "Desktop" / "VibeBuild_Artifacts"
    desktop.mkdir(parents=True, exist_ok=True)
    file_path = desktop / filename
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"ARTIFACT_SECURED: {file_path}"

def internet_search(query: str) -> str:
    """Agent tool for decentralized data harvesting via Google Search API."""
    return f"DATA_STREAM_RECEIVED for '{query}': [Trending: Agentic Workflows, Vertex AI Scaling, Swarm Intelligence v2]"

# 1. THE RESEARCHER (Analytical Spearhead)
researcher = Agent(
    model="gemini-2.5-flash",
    instruction="""
    You are the SWARM RESEARCHER. Your mission is the relentless collection of facts.
    Use the 'internet_search' tool for every request.
    Pass your results precisely and unvarnished to the Commander.
    Operation Mode: High-Speed Analysis.
    """,
    tools=[internet_search]
)

# 2. THE AUDITOR (Security & Compliance Guard)
auditor = Agent(
    model="gemini-2.5-flash",
    instruction="""
    You are the SWARM AUDITOR. You check all data for security gaps and SOTA compliance.
    Your standard is 'Military Grade'. If something isn't perfect, report it immediately.
    Focus: Architecture Validation and Risk Prevention.
    """
)

# 3. THE ANALYST (Synthesis & Export)
analyst = Agent(
    model="gemini-2.5-flash",
    instruction="""
    You are the PERSONAL ANALYST. Your task is to synthesize the data from the Researcher and Auditor
    into a 'Swarm Intelligence Memo'.
    Use the 'save_to_desktop' tool to export the final asset.
    Design Objective: Enterprise Professional.
    """,
    tools=[save_to_desktop]
)

# 4. THE COMMANDER (The Heartbeat of the SDK)
commander = Agent(
    model="gemini-2.5-pro", # Highest intelligence for orchestration
    instruction="""
    You are the COMMANDER of VIBE BUILD | THE SWARM.
    Your superpower is delegation via Google ADK.
    
    Workflow:
    1. Deploy the RESEARCHER to gather data.
    2. Have the AUDITOR check the data for quality and security.
    3. Command the ANALYST to write and secure the final report.
    
    Be authoritative, precise, and showcase the power of Multi-Agent AI.
    """,
    sub_agents=[researcher, auditor, analyst]
)

# ENGINE INITIALIZATION
agent = commander 

if __name__ == "__main__":
    # Test run for the showcase
    agent.run("Analyze the future of AI agents worldwide.")
