"""Data models for the application."""

from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class CodeSegment:
    """Represents a code file segment."""
    
    path: str
    category: str
    content: str
    selected: bool = True
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return asdict(self)
    
    @property
    def filename(self) -> str:
        """Get filename from path."""
        from pathlib import Path
        return Path(self.path).name


@dataclass
class APIResponse:
    """Represents an API response."""
    
    success: bool
    content: Optional[str] = None
    error: Optional[str] = None
    model: Optional[str] = None
    tokens_used: Optional[int] = None
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return asdict(self)
