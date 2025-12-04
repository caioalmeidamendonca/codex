#!/usr/bin/env python3
"""
AI DEBUG TOOL - Main Entry Point
A professional tool for generating optimized prompts for Claude AI.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.app import ClaudePromptGeneratorApp


def main():
    """Main entry point."""
    try:
        app = ClaudePromptGeneratorApp()
        app.run()
    except KeyboardInterrupt:
        print("\nAplicação encerrada pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"Erro fatal: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
