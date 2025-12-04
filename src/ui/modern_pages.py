"""Modern UI pages with enhanced visual design."""

import customtkinter as ctk
from tkinter import filedialog, messagebox
from typing import Callable, Dict
from pathlib import Path
from ..config import config, theme, CategoryConfig
from .modern_widgets import (
    ModernCard, GradientButton, ModernInput, ModernTextArea,
    IconLabel, ModernDivider, ModernProgressBar
)


class ModernBasePage(ctk.CTkFrame):
    """Modern base class for all pages."""
    
    def __init__(self, parent, **kwargs):
        """Initialize modern base page."""
        super().__init__(
            parent,
            fg_color=theme.BG_PRIMARY,
            corner_radius=0,
            **kwargs
        )
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


class ModernLoginPage(ModernBasePage):
    """Modern login/API configuration page."""
    
    def __init__(self, parent, on_login: Callable, on_test: Callable):
        """Initialize modern login page."""
        super().__init__(parent)
        
        # Center container
        center_container = ctk.CTkFrame(self, fg_color=theme.BG_PRIMARY)
        center_container.grid(row=0, column=0)
        
        # Modern card
        card = ModernCard(center_container, width=600)
        card.pack(padx=config.SPACING_XL, pady=config.SPACING_XL)
        
        # Content frame
        content = ctk.CTkFrame(card, fg_color=theme.BG_SECONDARY)
        content.pack(fill="both", expand=True, padx=config.SPACING_XL, pady=config.SPACING_XL)
        
        # Icon
        icon = ctk.CTkLabel(
            content,
            text="🔐",
            font=ctk.CTkFont(size=72)
        )
        icon.pack(pady=(config.SPACING_LG, config.SPACING_MD))
        
        # Title
        IconLabel(
            content,
            text="Configuração da API",
            size="hero",
            color="primary"
        ).pack(pady=(0, config.SPACING_SM))
        
        # Subtitle
        IconLabel(
            content,
            text="Configure sua API Key do Claude para começar",
            size="normal",
            color="secondary"
        ).pack(pady=(0, config.SPACING_XL))
        
        # API Key input
        self.api_key_entry = ModernInput(
            content,
            placeholder="Cole sua API Key aqui...",
            icon="🔑",
            show="•",
            width=500
        )
        self.api_key_entry.pack(pady=config.SPACING_MD)
        
        # Buttons
        btn_frame = ctk.CTkFrame(content, fg_color=theme.BG_SECONDARY)
        btn_frame.pack(pady=config.SPACING_LG)
        
        self.login_btn = GradientButton(
            btn_frame,
            text="Conectar",
            command=on_login,
            variant="primary",
            icon="🚀",
            width=220
        )
        self.login_btn.grid(row=0, column=0, padx=config.SPACING_SM)
        
        test_btn = GradientButton(
            btn_frame,
            text="Testar Conexão",
            command=on_test,
            variant="secondary",
            icon="🔍",
            width=220
        )
        test_btn.grid(row=0, column=1, padx=config.SPACING_SM)
        
        # Divider
        ModernDivider(content).pack(fill="x", pady=config.SPACING_LG)
        
        # Instructions card
        inst_card = ModernCard(content, width=500)
        inst_card.pack(pady=config.SPACING_MD)
        
        inst_content = ctk.CTkFrame(inst_card, fg_color=theme.BG_SECONDARY)
        inst_content.pack(fill="both", padx=config.SPACING_LG, pady=config.SPACING_LG)
        
        IconLabel(
            inst_content,
            text="Como obter sua API Key",
            icon="💡",
            size="large",
            color="accent"
        ).pack(anchor="w", pady=(0, config.SPACING_SM))
        
        instructions_text = """1. Acesse: https://console.anthropic.com/
2. Faça login ou crie uma conta
3. Navegue até "API Keys"
4. Clique em "Create Key"
5. Copie e cole acima

🔒 Sua API Key é confidencial e segura
✨ Armazenada apenas durante esta sessão"""
        
        inst_label = ctk.CTkLabel(
            inst_content,
            text=instructions_text,
            font=ctk.CTkFont(
                family=config.FONT_FAMILY,
                size=config.FONT_SIZE_SMALL
            ),
            text_color=theme.TEXT_SECONDARY,
            justify="left"
        )
        inst_label.pack(anchor="w")
    
    def get_api_key(self) -> str:
        """Get the entered API key."""
        return self.api_key_entry.get().strip()
    
    def set_loading(self, loading: bool):
        """Set loading state."""
        if loading:
            self.login_btn.configure(state="disabled", text="🔄 Conectando...")
        else:
            self.login_btn.configure(state="normal", text="🚀 Conectar")


class ModernPromptPage(ModernBasePage):
    """Modern prompt generation page."""
    
    def __init__(
        self,
        parent,
        on_generate: Callable,
        on_copy: Callable,
        on_save: Callable,
        on_send: Callable,
        on_clear: Callable
    ):
        """Initialize modern prompt page."""
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=2)
        
        # Header
        header = ctk.CTkFrame(self, fg_color=theme.BG_PRIMARY)
        header.grid(row=0, column=0, sticky="ew", pady=(0, config.SPACING_MD))
        
        IconLabel(
            header,
            text="Geração de Prompt",
            icon="✨",
            size="title",
            color="primary"
        ).pack(side="left")
        
        # Instructions section
        inst_card = ModernCard(self)
        inst_card.grid(row=1, column=0, sticky="nsew", pady=(0, config.SPACING_MD))
        inst_card.grid_rowconfigure(1, weight=1)
        inst_card.grid_columnconfigure(0, weight=1)
        
        IconLabel(
            inst_card,
            text="O que você quer que o Claude faça?",
            icon="💭",
            size="large",
            color="accent"
        ).grid(row=0, column=0, sticky="w", padx=config.SPACING_LG, pady=config.SPACING_MD)
        
        self.user_instructions = ModernTextArea(inst_card, height=120)
        self.user_instructions.grid(row=1, column=0, sticky="nsew", padx=config.SPACING_LG, pady=(0, config.SPACING_LG))
        self.user_instructions.insert(
            "1.0",
            "Exemplo: Analise este código e sugira melhorias de performance, segurança e boas práticas."
        )
        
        # Action buttons
        btn_frame = ctk.CTkFrame(self, fg_color=theme.BG_PRIMARY)
        btn_frame.grid(row=2, column=0, sticky="ew", pady=config.SPACING_MD)
        
        GradientButton(
            btn_frame,
            text="Gerar Preview",
            command=on_generate,
            variant="primary",
            icon="🔄",
            width=160
        ).pack(side="left", padx=config.SPACING_XS)
        
        GradientButton(
            btn_frame,
            text="Copiar",
            command=on_copy,
            variant="secondary",
            icon="📋",
            width=120
        ).pack(side="left", padx=config.SPACING_XS)
        
        GradientButton(
            btn_frame,
            text="Salvar",
            command=on_save,
            variant="secondary",
            icon="💾",
            width=120
        ).pack(side="left", padx=config.SPACING_XS)
        
        GradientButton(
            btn_frame,
            text="Limpar",
            command=on_clear,
            variant="danger",
            icon="🗑️",
            width=120
        ).pack(side="right", padx=config.SPACING_XS)
        
        self.send_btn = GradientButton(
            btn_frame,
            text="Enviar para Claude",
            command=on_send,
            variant="success",
            icon="🚀",
            width=200
        )
        self.send_btn.pack(side="right", padx=config.SPACING_XS)
        
        # Preview section
        preview_card = ModernCard(self)
        preview_card.grid(row=3, column=0, sticky="nsew")
        preview_card.grid_rowconfigure(1, weight=1)
        preview_card.grid_columnconfigure(0, weight=1)
        
        IconLabel(
            preview_card,
            text="Preview do Prompt",
            icon="👁️",
            size="large",
            color="accent"
        ).grid(row=0, column=0, sticky="w", padx=config.SPACING_LG, pady=config.SPACING_MD)
        
        self.prompt_preview = ModernTextArea(preview_card)
        self.prompt_preview.grid(row=1, column=0, sticky="nsew", padx=config.SPACING_LG, pady=(0, config.SPACING_LG))
        
        # Progress bar
        self.progress_bar = ModernProgressBar(self)
        self.progress_bar.grid(row=4, column=0, sticky="ew", pady=(config.SPACING_MD, 0))
        self.progress_bar.grid_remove()
    
    def get_user_instructions(self) -> str:
        """Get user instructions text."""
        return self.user_instructions.get("1.0", "end").strip()
    
    def set_user_instructions(self, text: str):
        """Set user instructions text."""
        self.user_instructions.delete("1.0", "end")
        self.user_instructions.insert("1.0", text)
    
    def get_prompt_preview(self) -> str:
        """Get prompt preview text."""
        return self.prompt_preview.get("1.0", "end").strip()
    
    def set_prompt_preview(self, text: str):
        """Set prompt preview text."""
        self.prompt_preview.delete("1.0", "end")
        self.prompt_preview.insert("1.0", text)
    
    def clear_all(self):
        """Clear all text fields."""
        self.user_instructions.delete("1.0", "end")
        self.prompt_preview.delete("1.0", "end")
    
    def show_progress(self, show: bool):
        """Show or hide progress bar."""
        if show:
            self.progress_bar.grid()
            self.progress_bar.start()
            self.send_btn.configure(state="disabled")
        else:
            self.progress_bar.stop()
            self.progress_bar.grid_remove()
            self.send_btn.configure(state="normal")


class ModernResultPage(ModernBasePage):
    """Modern results display page."""
    
    def __init__(
        self,
        parent,
        on_copy: Callable,
        on_save: Callable,
        on_apply: Callable
    ):
        """Initialize modern result page."""
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        
        # Header
        header = ctk.CTkFrame(self, fg_color=theme.BG_PRIMARY)
        header.grid(row=0, column=0, sticky="ew", pady=(0, config.SPACING_MD))
        
        IconLabel(
            header,
            text="Resposta do Claude",
            icon="💬",
            size="title",
            color="success"
        ).pack(side="left")
        
        # Action buttons
        btn_frame = ctk.CTkFrame(header, fg_color=theme.BG_PRIMARY)
        btn_frame.pack(side="right")
        
        GradientButton(
            btn_frame,
            text="Copiar",
            command=on_copy,
            variant="secondary",
            icon="📋",
            width=120
        ).pack(side="left", padx=config.SPACING_XS)
        
        GradientButton(
            btn_frame,
            text="Salvar",
            command=on_save,
            variant="secondary",
            icon="💾",
            width=120
        ).pack(side="left", padx=config.SPACING_XS)
        
        GradientButton(
            btn_frame,
            text="Aplicar",
            command=on_apply,
            variant="success",
            icon="✅",
            width=120
        ).pack(side="left", padx=config.SPACING_XS)
        
        # Result card
        result_card = ModernCard(self)
        result_card.grid(row=1, column=0, sticky="nsew")
        result_card.grid_rowconfigure(0, weight=1)
        result_card.grid_columnconfigure(0, weight=1)
        
        self.result_text = ModernTextArea(result_card)
        self.result_text.grid(row=0, column=0, sticky="nsew", padx=config.SPACING_LG, pady=config.SPACING_LG)
    
    def get_result(self) -> str:
        """Get result text."""
        return self.result_text.get("1.0", "end")
    
    def set_result(self, text: str):
        """Set result text."""
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", text)
