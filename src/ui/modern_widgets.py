"""Modern UI widgets with enhanced visual design."""

import customtkinter as ctk
from typing import Callable, Optional
from ..config import config, theme


class ModernCard(ctk.CTkFrame):
    """Modern card component with shadow effect."""
    
    def __init__(self, parent, **kwargs):
        """Initialize modern card."""
        super().__init__(
            parent,
            corner_radius=config.RADIUS_LG,
            fg_color=(theme.BG_SECONDARY, theme.BG_SECONDARY),
            border_width=1,
            border_color=(theme.BORDER, theme.BORDER),
            **kwargs
        )
        
        # Add hover effect
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
    
    def _on_enter(self, event):
        """Handle mouse enter."""
        if config.HOVER_ANIMATION:
            self.configure(border_color=theme.BORDER_LIGHT)
    
    def _on_leave(self, event):
        """Handle mouse leave."""
        if config.HOVER_ANIMATION:
            self.configure(border_color=theme.BORDER)


class GradientButton(ctk.CTkButton):
    """Modern button with gradient and animations."""
    
    def __init__(
        self,
        parent,
        text: str,
        command: Optional[Callable] = None,
        variant: str = "primary",
        icon: str = "",
        **kwargs
    ):
        """
        Initialize gradient button.
        
        Args:
            parent: Parent widget
            text: Button text
            command: Click handler
            variant: Style variant (primary, success, danger, secondary, ghost)
            icon: Optional emoji icon
        """
        # Style configurations
        styles = {
            'primary': {
                'fg_color': theme.PRIMARY,
                'hover_color': theme.PRIMARY_HOVER,
                'text_color': theme.TEXT_PRIMARY
            },
            'success': {
                'fg_color': theme.SUCCESS,
                'hover_color': theme.SUCCESS_HOVER,
                'text_color': theme.TEXT_PRIMARY
            },
            'danger': {
                'fg_color': theme.ERROR,
                'hover_color': theme.ERROR_HOVER,
                'text_color': theme.TEXT_PRIMARY
            },
            'warning': {
                'fg_color': theme.WARNING,
                'hover_color': theme.WARNING_HOVER,
                'text_color': theme.TEXT_PRIMARY
            },
            'secondary': {
                'fg_color': theme.BG_TERTIARY,
                'hover_color': theme.BG_HOVER,
                'text_color': theme.TEXT_PRIMARY,
                'border_width': 1,
                'border_color': theme.BORDER
            },
            'ghost': {
                'fg_color': theme.BG_PRIMARY,
                'hover_color': theme.BG_TERTIARY,
                'text_color': theme.TEXT_SECONDARY,
                'border_width': 2,
                'border_color': theme.BORDER
            }
        }
        
        style = styles.get(variant, styles['primary'])
        
        # Add icon to text if provided
        display_text = f"{icon} {text}" if icon else text
        
        super().__init__(
            parent,
            text=display_text,
            command=command,
            height=44,
            corner_radius=config.RADIUS_MD,
            font=ctk.CTkFont(
                family=config.FONT_FAMILY,
                size=config.FONT_SIZE_NORMAL,
                weight="bold"
            ),
            **{**style, **kwargs}
        )


class ModernStatusBadge(ctk.CTkFrame):
    """Modern status badge with color coding."""
    
    def __init__(self, parent, text: str = "Ready", status: str = "idle", **kwargs):
        """Initialize status badge."""
        super().__init__(
            parent,
            corner_radius=config.RADIUS_SM,
            fg_color=theme.BG_TERTIARY,
            **kwargs
        )
        
        self.status_colors = {
            'idle': (theme.TEXT_MUTED, theme.BG_TERTIARY),
            'connected': (theme.SUCCESS, theme.BG_TERTIARY),
            'error': (theme.ERROR, theme.BG_TERTIARY),
            'loading': (theme.WARNING, theme.BG_TERTIARY),
            'info': (theme.INFO, theme.BG_TERTIARY)
        }
        
        # Dot indicator
        self.dot = ctk.CTkLabel(
            self,
            text="●",
            font=ctk.CTkFont(size=16),
            width=20
        )
        self.dot.pack(side="left", padx=(5, 0))
        
        # Status text
        self.label = ctk.CTkLabel(
            self,
            text=text,
            font=ctk.CTkFont(
                family=config.FONT_FAMILY,
                size=config.FONT_SIZE_SMALL,
                weight="bold"
            )
        )
        self.label.pack(side="left", padx=(0, 5))
        
        self.set_status(status, text)
    
    def set_status(self, status: str, text: str = None):
        """Update status."""
        color, bg = self.status_colors.get(status, self.status_colors['idle'])
        self.dot.configure(text_color=color)
        self.configure(fg_color=bg)
        if text:
            self.label.configure(text=text)


class ModernProgressBar(ctk.CTkFrame):
    """Modern progress bar with smooth animation."""
    
    def __init__(self, parent, **kwargs):
        """Initialize progress bar."""
        super().__init__(
            parent,
            height=4,
            corner_radius=2,
            fg_color=theme.BG_TERTIARY,
            **kwargs
        )
        
        self.progress = ctk.CTkProgressBar(
            self,
            mode="indeterminate",
            corner_radius=2,
            height=4,
            progress_color=theme.PRIMARY
        )
        self.progress.pack(fill="both", expand=True)
        self.progress.set(0)
    
    def start(self):
        """Start progress animation."""
        self.progress.start()
    
    def stop(self):
        """Stop progress animation."""
        self.progress.stop()


class ModernInput(ctk.CTkEntry):
    """Modern input field with enhanced styling."""
    
    def __init__(
        self,
        parent,
        placeholder: str = "",
        icon: str = "",
        **kwargs
    ):
        """Initialize modern input."""
        super().__init__(
            parent,
            placeholder_text=f"{icon} {placeholder}" if icon else placeholder,
            height=44,
            corner_radius=config.RADIUS_MD,
            border_width=2,
            border_color=theme.BORDER,
            fg_color=theme.BG_TERTIARY,
            text_color=theme.TEXT_PRIMARY,
            placeholder_text_color=theme.TEXT_MUTED,
            font=ctk.CTkFont(
                family=config.FONT_FAMILY,
                size=config.FONT_SIZE_NORMAL
            ),
            **kwargs
        )
        
        # Add focus effects
        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)
    
    def _on_focus_in(self, event):
        """Handle focus in."""
        self.configure(border_color=theme.PRIMARY)
    
    def _on_focus_out(self, event):
        """Handle focus out."""
        self.configure(border_color=theme.BORDER)


class ModernTextArea(ctk.CTkTextbox):
    """Modern text area with enhanced styling."""
    
    def __init__(self, parent, **kwargs):
        """Initialize modern text area."""
        super().__init__(
            parent,
            corner_radius=config.RADIUS_MD,
            border_width=2,
            border_color=theme.BORDER,
            fg_color=theme.BG_TERTIARY,
            text_color=theme.TEXT_PRIMARY,
            font=ctk.CTkFont(
                family=config.FONT_FAMILY,
                size=config.FONT_SIZE_NORMAL
            ),
            wrap="word",
            **kwargs
        )
        
        # Add focus effects
        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)
    
    def _on_focus_in(self, event):
        """Handle focus in."""
        self.configure(border_color=theme.PRIMARY)
    
    def _on_focus_out(self, event):
        """Handle focus out."""
        self.configure(border_color=theme.BORDER)


class IconLabel(ctk.CTkLabel):
    """Label with icon and modern styling."""
    
    def __init__(
        self,
        parent,
        text: str,
        icon: str = "",
        size: str = "normal",
        color: str = "primary",
        **kwargs
    ):
        """Initialize icon label."""
        sizes = {
            'small': config.FONT_SIZE_SMALL,
            'normal': config.FONT_SIZE_NORMAL,
            'large': config.FONT_SIZE_LARGE,
            'title': config.FONT_SIZE_TITLE,
            'hero': config.FONT_SIZE_HERO
        }
        
        colors = {
            'primary': theme.TEXT_PRIMARY,
            'secondary': theme.TEXT_SECONDARY,
            'muted': theme.TEXT_MUTED,
            'accent': theme.ACCENT,
            'success': theme.SUCCESS,
            'error': theme.ERROR
        }
        
        display_text = f"{icon} {text}" if icon else text
        
        super().__init__(
            parent,
            text=display_text,
            font=ctk.CTkFont(
                family=config.FONT_FAMILY,
                size=sizes.get(size, config.FONT_SIZE_NORMAL),
                weight="bold" if size in ['title', 'hero'] else "normal"
            ),
            text_color=colors.get(color, theme.TEXT_PRIMARY),
            **kwargs
        )


class ModernTooltip:
    """Modern tooltip component."""
    
    def __init__(self, widget, text: str):
        """Initialize tooltip."""
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        
        widget.bind("<Enter>", self.show_tooltip)
        widget.bind("<Leave>", self.hide_tooltip)
    
    def show_tooltip(self, event=None):
        """Show tooltip."""
        if self.tooltip_window or not self.text:
            return
        
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        
        self.tooltip_window = tw = ctk.CTkToplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        
        label = ctk.CTkLabel(
            tw,
            text=self.text,
            fg_color=theme.BG_SECONDARY,
            corner_radius=config.RADIUS_SM,
            font=ctk.CTkFont(size=config.FONT_SIZE_SMALL),
            text_color=theme.TEXT_PRIMARY
        )
        label.pack(padx=8, pady=6)
    
    def hide_tooltip(self, event=None):
        """Hide tooltip."""
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None


class ModernDivider(ctk.CTkFrame):
    """Modern divider line."""
    
    def __init__(self, parent, orientation: str = "horizontal", **kwargs):
        """Initialize divider."""
        if orientation == "horizontal":
            super().__init__(
                parent,
                height=1,
                fg_color=theme.BORDER,
                **kwargs
            )
        else:
            super().__init__(
                parent,
                width=1,
                fg_color=theme.BORDER,
                **kwargs
            )


class ModernSwitch(ctk.CTkSwitch):
    """Modern switch toggle."""
    
    def __init__(self, parent, text: str = "", command: Optional[Callable] = None, **kwargs):
        """Initialize switch."""
        super().__init__(
            parent,
            text=text,
            command=command,
            progress_color=theme.PRIMARY,
            button_color=theme.TEXT_PRIMARY,
            button_hover_color=theme.TEXT_SECONDARY,
            fg_color=theme.BG_TERTIARY,
            font=ctk.CTkFont(
                family=config.FONT_FAMILY,
                size=config.FONT_SIZE_NORMAL
            ),
            **kwargs
        )
