# multion-hackathon - DevLog

Records debugging steps from chatgpt on Notion  🚀

## How to run

Prerequisite: Ensure that you have `poetry` installed: [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

1. Make sure that the MultiOn Chrome Extension is installed and enabled (for more details, see [here](https://docs.multion.ai/learn/browser-extension)).

2. Create a .env file and store the following variables:

```bash
OPENAI_API_KEY=<your-openai-api-key>
MULTION_API_KEY=<your-multion-api-key>
AGENTOPS_API_KEY=<your-multion-api-key>
```

3. Install required packages with poetry:

```bash
poetry install
```

4. Run the note taker! Make sure that you are logged into Notion.

```bash
poetry run python note_taker.py
```
