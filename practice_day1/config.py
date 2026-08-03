"""Shared configuration for the coding agent."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Path to the repository we'll analyze
REPO_PATH = Path(__file__).parent.parent / "sample_repo"

# Default LLM for all agents in this workshop — served locally via Ollama
LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-oss:20b")
LLM_BASE_URL = os.environ.get("LLM_BASE_URL", "http://192.168.88.246:11434/v1")
LLM_API_KEY = os.environ.get("LLM_API_KEY", "ollama")
