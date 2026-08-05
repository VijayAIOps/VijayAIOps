# Incident Summarizer AI

An AI-powered agent that generates concise summaries, timelines, and action items from incident data.

## Features
- Summarizes incidents into 3–6 bullet points
- Builds a timeline of key events
- Extracts action items with owners and due dates
- Works locally with Python

## Setup

1. Clone the repo:
   git clone https://github.com/<your-username>/incident-summarizer-ai.git

2. Create virtual environment:
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Add your API key:
   cp .env.example .env
   Add your OPENAI_API_KEY inside .env

## Run
python src/main.py