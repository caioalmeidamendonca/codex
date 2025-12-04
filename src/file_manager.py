"""File management and scanning module."""

import os
from pathlib import Path
from typing import List, Optional, Set
from .models import CodeSegment
from .config import config


class FileManager:
    """Manages file operations and project scanning."""
    
    def __init__(self):
        """Initialize the file manager."""
        self.project_path: str = ""
        self.code_segments: List[CodeSegment] = []
    
    def set_project_path(self, path: str) -> bool:
        """
        Set the project path.
        
        Args:
            path: Path to the project directory
            
        Returns:
            True if path is valid, False otherwise
        """
        if os.path.isdir(path):
            self.project_path = path
            return True
        return False
    
    def scan_directory(self, path: Optional[str] = None) -> str:
        """
        Scan directory and return tree structure.
        
        Args:
            path: Path to scan (uses project_path if None)
            
        Returns:
            String representation of directory tree
        """
        scan_path = path or self.project_path
        if not scan_path or not os.path.isdir(scan_path):
            return "No valid directory to scan"
        
        tree_lines = []
        tree_lines.append(f"📂 {Path(scan_path).name}\n")
        
        def scan_dir(current_path: str, prefix: str = ""):
            """Recursively scan directory."""
            try:
                items = sorted(
                    Path(current_path).iterdir(),
                    key=lambda x: (not x.is_dir(), x.name.lower())
                )
                
                for idx, item in enumerate(items):
                    if item.name in config.IGNORE_DIRS:
                        continue
                    
                    is_last = idx == len(items) - 1
                    connector = "└── " if is_last else "├── "
                    
                    if item.is_dir():
                        tree_lines.append(f"{prefix}{connector}📁 {item.name}\n")
                        extension = "    " if is_last else "│   "
                        scan_dir(str(item), prefix + extension)
                    elif item.suffix in config.CODE_EXTENSIONS:
                        size = item.stat().st_size
                        size_str = f"{size/1024:.1f}KB" if size > 1024 else f"{size}B"
                        tree_lines.append(f"{prefix}{connector}📄 {item.name} ({size_str})\n")
                        
            except PermissionError:
                pass
        
        scan_dir(scan_path)
        return "".join(tree_lines)
    
    def add_file(self, filepath: str, category: str) -> bool:
        """
        Add a file to code segments.
        
        Args:
            filepath: Path to the file
            category: Category for the file
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            segment = CodeSegment(
                path=filepath,
                category=category,
                content=content,
                selected=True
            )
            
            self.code_segments.append(segment)
            return True
            
        except Exception as e:
            print(f"Error reading file {filepath}: {e}")
            return False
    
    def remove_files_by_category(self, category: str) -> int:
        """
        Remove all files from a category.
        
        Args:
            category: Category to remove
            
        Returns:
            Number of files removed
        """
        initial_count = len(self.code_segments)
        self.code_segments = [
            s for s in self.code_segments 
            if s.category != category
        ]
        return initial_count - len(self.code_segments)
    
    def get_files_by_category(self, category: str) -> List[CodeSegment]:
        """
        Get all files in a category.
        
        Args:
            category: Category to filter by
            
        Returns:
            List of code segments
        """
        return [s for s in self.code_segments if s.category == category]
    
    def get_all_categories(self) -> Set[str]:
        """Get all categories currently in use."""
        return {s.category for s in self.code_segments}
    
    def clear_all(self):
        """Clear all code segments."""
        self.code_segments.clear()
    
    def get_segment_count(self) -> int:
        """Get total number of segments."""
        return len(self.code_segments)
    
    def get_total_size(self) -> int:
        """Get total size of all segments in bytes."""
        return sum(len(s.content) for s in self.code_segments)
