# DevLog

Logs debugging steps from chatgpt on Notion  🚀

## What does DevLog mean?

I named this project DevLog because its a developer logging tool aka notes taking tool
This project was began at a [hackathon](https://lu.ma/ai-agents-2.0?tk=36NHJB) that I joined from July 20 - July 21 2024 that I am still continuing development on.
[Check out the slides](https://docs.google.com/presentation/d/14rrUprHQya8ZeVnUZJa3k7JcwZ33gGzgg-bjTa2g1oo/edit?usp=sharing)


## Inspiration

Throughout my years of being a generalist engineer, I have been writing down bugs I encountered in notion, I refer to it from time to time when I face the same issues. I call it [Chiayi's personal knowledge base](https://grape-wolf-71f.notion.site/bebb78024ff9423d9121d010f2b848c5?v=13a5b21ed1ca4bee83258bf0dcb22dae&pvs=4).
This project will help me automate some of the process.

## See DevLog in action
[Watch this demo video](https://www.loom.com/share/3fa6e41b0dcd4be6b2cba05cdbe77880)

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
