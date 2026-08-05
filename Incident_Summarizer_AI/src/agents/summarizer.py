from dotenv import load_dotenv
load_dotenv()  # Load .env BEFORE anything else

import os
import json
from openai import OpenAI

# Initialize OpenAI client using the API key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# System prompt for the AI summarizer
SYSTEM_PROMPT = """
You are an AI assistant that summarizes incident reports.
Your tasks:
1. Provide a concise summary (3–6 bullet points).
2. Provide a timeline of key events.
3. Extract action items with owners and due dates (if available).

Return ONLY valid JSON with keys:
- summary
- timeline
- action_items
"""

def build_user_prompt(incident):
    meta = f"""
Incident ID: {incident['incident_id']}
Title: {incident['title']}
Severity: {incident['severity']}
Status: {incident['status']}
Created At: {incident['created_at']}
Updated At: {incident['updated_at']}
"""

    details = f"""
Incident Description:
{incident['description']}

Root Cause:
{incident['root_cause']}

Impact:
{incident['impact']}

Resolution:
{incident['resolution']}
"""

    return meta + "\n" + details


def summarize_incident(incident):
    user_prompt = build_user_prompt(incident)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ]
    )

    # Extract the model's JSON output
    ai_output = response.choices[0].message.content

    try:
        return json.loads(ai_output)
    except json.JSONDecodeError:
        return {
            "summary": ["AI response was not valid JSON"],
            "timeline": [],
            "action_items": []
        }