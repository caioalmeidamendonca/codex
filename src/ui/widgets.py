"""Reusable UI widgets."""

import customtkinter as ctk
from typing import Callable, Optional


class StatusIndicator(ctk.CTkLabel):
    """Status indicator widget with color coding."""
    
    def __init__(self, parent, **kwargs):
        """Initialize status indicator."""
        super().__init__(
            parent,
            text="● Desconectado",
            font=ctk.CTkFont(size=12),
            text_color="#ef4444",
            **kwargs
        )
    
    def set_connected(self):
        """Set to connected state."""
        self.configure(text="● Conectado", text_color="#10b981")
    
    def set_disconnected(self):
        """Set to disconnected state."""
        self.configure(text="● Desconectado", text_color="#ef4444")
    
    def set_error(self):
        """Set to error state."""
        self.configure(text="● Erro", text_color="#ef4444")
    
    def set_loading(self):
        """Set to loading state."""
        self.configure(text="● Processando...", text_color="#f59e0b")


class ActionButton(ctk.CTkButton):
    """Styled action button with consistent appearance."""
    
    def __init__(
        self,
        parent,
        text: str,
        command: Optional[Callable] = None,
        variant: str = "primary",
        **kwargs
    ):
        """
        Initialize action button.
        
        Args:
            parent: Parent widget
            text: Button text
            command: Click handler
            variant: Style variant (primary, secondary, danger, success)
        """
        styles = {
            'primary': {
                'fg_color': None,
                'hover_color': None
            },
            'secondary': {
                'fg_color': 'transparent',
                'border_width': 2,
                'hover_color': ("gray70", "gray30")
            },
            'danger': {
                'fg_color': '#ef4444',
                'hover_color': '#dc2626'
            },
            'success': {
                'fg_color': '#10b981',
                'hover_color': '#059669'
            }
        }
        
        style = styles.get(variant, styles['primary'])
        
        super().__init__(
            parent,
            text=text,
            command=command,
            height=40,
            font=ctk.CTkFont(size=14),
            corner_radius=10,
            **{**style, **kwargs}
        )


class PageHeader(ctk.CTkFrame):
    """Page header with title and optional buttons."""
    
    def __init__(self, parent, title: str, **kwargs):
        """Initialize page header."""
        super().__init__(parent, fg_color="transparent", **kwargs)
        
        self.title_label = ctk.CTkLabel(
            self,
            text=title,
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.pack(side="left")
        
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(side="right")
    
    def add_button(self, text: str, command: Callable, **kwargs) -> ctk.CTkButton:
        """Add a button to the header."""
        btn = ctk.CTkButton(
            self.button_frame,
            text=text,
            command=command,
            height=35,
            font=ctk.CTkFont(size=13),
            **kwargs
        )
        btn.pack(side="left", padx=5)
        return btn


class CategoryCard(ctk.CTkFrame):
    """Card widget for file categories."""
    
    def __init__(
        self,
        parent,
        label: str,
        category_key: str,
        on_add: Callable,
        on_remove: Callable,
        **kwargs
    ):
        """Initialize category card."""
        super().__init__(parent, **kwargs)
        
        self.category_key = category_key
        
        # Header
        header = ctk.CTkLabel(
            self,
            text=label,
            font=ctk.CTkFont(size=13, weight="bold")
        )
        header.pack(anchor="w", padx=10, pady=5)
        
        # File list
        listbox_frame = ctk.CTkFrame(self, fg_color=("gray95", "gray10"))
        listbox_frame.pack(fill="x", padx=10, pady=(0, 5))
        
        self.textbox = ctk.CTkTextbox(
            listbox_frame,
            height=60,
            font=ctk.CTkFont(size=11)
        )
        self.textbox.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Buttons
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(fill="x", padx=10, pady=(0, 5))
        
        add_btn = ctk.CTkButton(
            btn_frame,
            text="← Adicionar",
            command=lambda: on_add(category_key),
            height=28,
            font=ctk.CTkFont(size=11)
        )
        add_btn.pack(side="left", padx=2)
        
        remove_btn = ctk.CTkButton(
            btn_frame,
            text="Remover",
            command=lambda: on_remove(category_key),
            height=28,
            font=ctk.CTkFont(size=11),
            fg_color="transparent",
            border_width=1
        )
        remove_btn.pack(side="left", padx=2)
    
    def add_file(self, filename: str):
        """Add a file to the list."""
        self.textbox.insert("end", f"✓ {filename}\n")
    
    def clear(self):
        """Clear all files."""
        self.textbox.delete("1.0", "end")
    
    def get_content(self) -> str:
        """Get textbox content."""
        return self.textbox.get("1.0", "end")


class ToolCard(ctk.CTkFrame):
    """Card widget for documentation tools."""
    
    def __init__(
        self,
        parent,
        icon: str,
        title: str,
        description: str,
        command: Callable,
        **kwargs
    ):
        """Initialize tool card."""
        super().__init__(parent, corner_radius=15, **kwargs)
        
        # Icon
        icon_label = ctk.CTkLabel(
            self,
            text=icon,
            font=ctk.CTkFont(size=40)
        )
        icon_label.pack(pady=(20, 10))
        
        # Title
        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=ctk.CTkFont(size=18, weight="bold")
        )
        title_label.pack()
        
        # Description
        desc_label = ctk.CTkLabel(
            self,
            text=description,
            font=ctk.CTkFont(size=13),
            text_color=("gray40", "gray60")
        )
        desc_label.pack(pady=5)
        
        # Action button
        action_btn = ctk.CTkButton(
            self,
            text="Executar",
            command=command,
            height=40,
            font=ctk.CTkFont(size=14),
            corner_radius=10
        )
        action_btn.pack(pady=20)
