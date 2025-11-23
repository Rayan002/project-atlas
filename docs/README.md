cat > README.md << 'EOF'

https://claude.ai/public/artifacts/17cfc4ea-3349-431e-be56-38ea7df826e2

# 🌍 Project Atlas: Distributed AI Trip Planner

A modular, multi-server AI system capable of planning end-to-end travel itineraries by orchestrating distinct micro-agents (MCP Servers).

## Architecture

Hub-and-Spoke architecture with:

- **Hub (Client):** LangGraph Supervisor
- **Spokes (Servers):** 5 Independent MCP servers

### The Server Ecosystem

1. **Intelligence Server**: Web search for destination info
2. **Aviation Server**: Flight data provider
3. **Hospitality Server**: Accommodation search
4. **Treasury Server**: Currency & budget management
5. **Memory Server**: Wishlist & itinerary storage with AI Sampling

## Quick Start

### Prerequisites

- Python 3.10+
- UV package manager
- Node.js (for MCP Inspector)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/project-atlas.git
cd project-atlas
```

2. Install dependencies with UV:

```bash
uv sync
```

3. Copy environment variables:

```bash
cp .env.example .env
# Edit .env with your API keys
```

4. Test a server with MCP Inspector:

```bash
npx @modelcontextprotocol/inspector uv run servers/intelligence/server.py
```

## Development

### Running tests

```bash
uv run pytest
```

### Linting

```bash
uv run black .
uv run ruff check .
```

### Type checking

```bash
uv run mypy .
```

## Project Status

- [ ] Step 1: Intelligence Server (FastMCP)
- [ ] Step 2: Aviation & Hospitality Servers
- [ ] Step 3: Treasury Server (Base MCP SDK)
- [ ] Step 4: Memory Server (with Sampling)
- [ ] Step 5: LangGraph Client

## Documentation

See the `docs/` folder for detailed documentation.

## License

MIT
EOF
