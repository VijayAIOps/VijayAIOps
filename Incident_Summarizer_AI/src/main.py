import json
from agents.summarizer import summarize_incident

def main():
    with open("src/examples/sampleincident.json") as f:
        incident = json.load(f)

    result = summarize_incident(incident)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
