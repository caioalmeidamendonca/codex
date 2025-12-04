"""Configuration management module."""

import os
from pathlib import Path
from typing import Set, Dict
from dataclasses import dataclass


@dataclass
class ModernTheme:
    """Modern color theme configuration."""
    
    # Primary colors
    PRIMARY: str = "#6366f1"  # Indigo
    PRIMARY_HOVER: str = "#4f46e5"
    PRIMARY_LIGHT: str = "#818cf8"
    
    # Accent colors
    ACCENT: str = "#8b5cf6"  # Purple
    ACCENT_HOVER: str = "#7c3aed"
    
    # Success/Error/Warning
    SUCCESS: str = "#10b981"
    SUCCESS_HOVER: str = "#059669"
    ERROR: str = "#ef4444"
    ERROR_HOVER: str = "#dc2626"
    WARNING: str = "#f59e0b"
    WARNING_HOVER: str = "#d97706"
    INFO: str = "#3b82f6"
    INFO_HOVER: str = "#2563eb"
    
    # Neutral colors (dark mode)
    BG_PRIMARY: str = "#0f172a"  # Slate 900
    BG_SECONDARY: str = "#1e293b"  # Slate 800
    BG_TERTIARY: str = "#334155"  # Slate 700
    BG_HOVER: str = "#475569"  # Slate 600
    
    # Text colors
    TEXT_PRIMARY: str = "#f1f5f9"  # Slate 100
    TEXT_SECONDARY: str = "#cbd5e1"  # Slate 300
    TEXT_MUTED: str = "#94a3b8"  # Slate 400
    
    # Border colors
    BORDER: str = "#334155"
    BORDER_LIGHT: str = "#475569"
    
    # Gradients
    GRADIENT_PRIMARY: str = "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
    GRADIENT_ACCENT: str = "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"
    GRADIENT_SUCCESS: str = "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)"


@dataclass
class AppConfig:
    """Application configuration."""
    
    # Window settings
    WINDOW_TITLE: str = "CODEX - AI Code Assistant"
    WINDOW_WIDTH: int = 1600
    WINDOW_HEIGHT: int = 1000
    WINDOW_MIN_WIDTH: int = 1200
    WINDOW_MIN_HEIGHT: int = 800
    
    # Theme settings
    APPEARANCE_MODE: str = "dark"
    COLOR_THEME: str = "blue"
    
    # API settings
    DEFAULT_MODEL: str = "claude-sonnet-4-5-20250929"
    MAX_TOKENS: int = 8000
    TEST_MAX_TOKENS: int = 10
    
    # UI Animation settings
    ANIMATION_DURATION: int = 200  # milliseconds
    HOVER_ANIMATION: bool = True
    SMOOTH_SCROLL: bool = True
    
    # Typography
    FONT_FAMILY: str = "Segoe UI"
    FONT_SIZE_SMALL: int = 11
    FONT_SIZE_NORMAL: int = 13
    FONT_SIZE_LARGE: int = 15
    FONT_SIZE_XLARGE: int = 18
    FONT_SIZE_TITLE: int = 24
    FONT_SIZE_HERO: int = 32
    
    # Spacing
    SPACING_XS: int = 5
    SPACING_SM: int = 10
    SPACING_MD: int = 15
    SPACING_LG: int = 20
    SPACING_XL: int = 30
    
    # Border radius
    RADIUS_SM: int = 8
    RADIUS_MD: int = 12
    RADIUS_LG: int = 16
    RADIUS_XL: int = 20
    
    # Sidebar
    SIDEBAR_WIDTH: int = 300
    SIDEBAR_COLLAPSED_WIDTH: int = 80
    
    # File settings
    CODE_EXTENSIONS: Set[str] = None
    IGNORE_DIRS: Set[str] = None
    
    def __post_init__(self):
        """Initialize complex default values."""
        if self.CODE_EXTENSIONS is None:
            self.CODE_EXTENSIONS = {
                '.py', '.js', '.jsx', '.ts', '.tsx', '.java', '.cpp',
                '.c', '.h', '.cs', '.php', '.rb', '.go', '.rs', '.swift',
                '.kt', '.html', '.css', '.scss', '.sql', '.json', '.xml',
                '.yaml', '.yml', '.md', '.txt', '.vue', '.svelte'
            }
        
        if self.IGNORE_DIRS is None:
            self.IGNORE_DIRS = {
                '.git', '__pycache__', 'node_modules', '.venv', 'venv',
                'build', 'dist', '.idea', '.vscode', 'env', '.pytest_cache',
                '.mypy_cache', 'coverage', '.tox', 'eggs', '.eggs'
            }


class CategoryConfig:
    """Category configuration for code organization."""
    
    CATEGORIES = {
        'database': '🗄️ Banco de Dados',
        'backend': '⚙️ Backend',
        'frontend': '🎨 Frontend',
        'models': '📝 Modelos',
        'utils': '🔧 Utilitários',
        'tests': '🧪 Testes',
        'config': '📋 Config',
        'docs': '📚 Docs',
        'api': '🔌 API',
        'other': '🎯 Outro'
    }
    
    @classmethod
    def get_display_name(cls, category: str) -> str:
        """Get display name for category."""
        return cls.CATEGORIES.get(category, category)
    
    @classmethod
    def get_all_categories(cls) -> list:
        """Get all categories as list of tuples."""
        return [(name, key) for key, name in cls.CATEGORIES.items()]


# Global configuration instances
config = AppConfig()
theme = ModernTheme()

# Application metadata
APP_NAME = "CODEX"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "AI-Powered Code Assistant with Claude Integration"
