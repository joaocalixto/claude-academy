# Claude Academy

My study notes and exercises from Anthropic's **Claude Academy** courses.

## Structure

```
claude-academy/
└── building-with-the-claude-api/
    └── code/          # Python examples using the Anthropic SDK
        ├── main.py
        ├── pyproject.toml
        └── .env.example
```

## Building with the Claude API

Examples that call the Claude API through the official Python SDK (`anthropic`).

### Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- An API key from the [Claude Console](https://console.anthropic.com/)

### Running

```bash
cd building-with-the-claude-api/code
cp .env.example .env          # then put your key in .env
uv sync
uv run main.py
```

> `main.py` loads `.env` with `override=True`, so the key in `.env` wins over any `ANTHROPIC_API_KEY` already set in your shell.

## Security

`.env` and API key files are listed in `.gitignore`. Never commit keys.
