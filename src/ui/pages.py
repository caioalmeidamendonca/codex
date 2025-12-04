"""UI page components."""

import customtkinter as ctk
from tkinter import filedialog, messagebox
from typing import Callable, Dict
from pathlib import Path
from ..config import CategoryConfig
from .widgets import PageHeader, CategoryCard, ToolCard, ActionButton


class BasePage(ctk.CTkFrame):
    """Base class for all pages."""
    
    def __init__(self, parent, **kwargs):
        """Initialize base page."""
        super().__init__(parent, fg_color="transparent", **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


class LoginPage(BasePage):
    """Login/API configuration page."""
    
    def __init__(self, parent, on_login: Callable, on_test: Callable):
        """Initialize login page."""
        super().__init__(parent)
        
        # Center frame
        center_frame = ctk.CTkFrame(
            self,
            fg_color=("gray90", "gray13"),
            corner_radius=20
        )
        center_frame.grid(row=0, column=0)
        center_frame.grid_columnconfigure(0, weight=1)
        
        # Icon
        icon_label = ctk.CTkLabel(
            center_frame,
            text="🤖",
            font=ctk.CTkFont(size=60)
        )
        icon_label.grid(row=0, column=0, pady=(40, 10))
        
        # Title
        title = ctk.CTkLabel(
            center_frame,
            text="Claude API Configuration",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title.grid(row=1, column=0, pady=(0, 10))
        
        # Subtitle
        subtitle = ctk.CTkLabel(
            center_frame,
            text="Configure sua API Key para começar",
            font=ctk.CTkFont(size=14),
            text_color=("gray40", "gray60")
        )
        subtitle.grid(row=2, column=0, pady=(0, 30))
        
        # API Key entry
        self.api_key_entry = ctk.CTkEntry(
            center_frame,
            width=500,
            height=45,
            placeholder_text="Cole sua API Key aqui...",
            show="•",
            font=ctk.CTkFont(size=14)
        )
        self.api_key_entry.grid(row=3, column=0, padx=40, pady=10)
        
        # Buttons
        btn_frame = ctk.CTkFrame(center_frame, fg_color="transparent")
        btn_frame.grid(row=4, column=0, pady=20)
        
        self.login_btn = ctk.CTkButton(
            btn_frame,
            text="Conectar",
            command=on_login,
            width=200,
            height=45,
            font=ctk.CTkFont(size=15, weight="bold"),
            corner_radius=10
        )
        self.login_btn.grid(row=0, column=0, padx=10)
        
        test_btn = ctk.CTkButton(
            btn_frame,
            text="Testar Conexão",
            command=on_test,
            width=200,
            height=45,
            font=ctk.CTkFont(size=15),
            fg_color="transparent",
            border_width=2,
            corner_radius=10
        )
        test_btn.grid(row=0, column=1, padx=10)
        
        # Instructions
        instructions = ctk.CTkTextbox(
            center_frame,
            width=500,
            height=200,
            font=ctk.CTkFont(size=12),
            fg_color=("gray95", "gray10")
        )
        instructions.grid(row=5, column=0, padx=40, pady=(20, 40))
        
        instructions_text = """Como obter sua API Key:

1. Acesse: https://console.anthropic.com/
2. Faça login ou crie uma conta
3. Vá em "API Keys"
4. Clique em "Create Key"
5. Copie e cole acima

💡 Dica: Sua API Key é confidencial e será armazenada
apenas durante esta sessão.

🔒 Seus dados estão seguros e não são compartilhados."""
        
        instructions.insert("1.0", instructions_text)
        instructions.configure(state="disabled")
    
    def get_api_key(self) -> str:
        """Get the entered API key."""
        return self.api_key_entry.get().strip()
    
    def set_loading(self, loading: bool):
        """Set loading state."""
        if loading:
            self.login_btn.configure(state="disabled", text="Conectando...")
        else:
            self.login_btn.configure(state="normal", text="Conectar")


class FilesPage(BasePage):
    """File management page."""
    
    def __init__(
        self,
        parent,
        on_open: Callable,
        on_refresh: Callable,
        on_add: Callable,
        on_remove: Callable
    ):
        """Initialize files page."""
        super().__init__(parent)
        self.grid_rowconfigure(2, weight=1)
        
        # Header
        header = PageHeader(self, "Gerenciamento de Arquivos")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 15))
        
        header.add_button("📂 Abrir Repositório", on_open)
        header.add_button(
            "🔄 Atualizar",
            on_refresh,
            fg_color="transparent",
            border_width=2
        )
        
        # Project path label
        self.project_path_label = ctk.CTkLabel(
            self,
            text="Nenhum projeto aberto",
            font=ctk.CTkFont(size=13),
            text_color=("gray40", "gray60"),
            anchor="w"
        )
        self.project_path_label.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        
        # Content frame
        content_frame = ctk.CTkFrame(self)
        content_frame.grid(row=2, column=0, sticky="nsew")
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        
        # Files panel
        files_panel = ctk.CTkFrame(content_frame)
        files_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        
        files_label = ctk.CTkLabel(
            files_panel,
            text="📁 Estrutura do Projeto",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        files_label.pack(pady=10)
        
        self.files_textbox = ctk.CTkTextbox(
            files_panel,
            font=ctk.CTkFont(size=12, family="Courier")
        )
        self.files_textbox.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        # Category panel
        category_panel = ctk.CTkFrame(content_frame)
        category_panel.grid(row=0, column=1, sticky="nsew", padx=(5, 0))
        
        cat_label = ctk.CTkLabel(
            category_panel,
            text="🏷️ Categorias",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        cat_label.pack(pady=10)
        
        self.category_scroll = ctk.CTkScrollableFrame(category_panel)
        self.category_scroll.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        # Create category cards
        self.category_widgets: Dict[str, CategoryCard] = {}
        for label, key in CategoryConfig.get_all_categories():
            card = CategoryCard(
                self.category_scroll,
                label=label,
                category_key=key,
                on_add=on_add,
                on_remove=on_remove
            )
            card.pack(fill="x", pady=5)
            self.category_widgets[key] = card
    
    def set_project_path(self, path: str):
        """Set the project path display."""
        self.project_path_label.configure(text=f"📂 {path}")
    
    def set_files_content(self, content: str):
        """Set the files textbox content."""
        self.files_textbox.delete("1.0", "end")
        self.files_textbox.insert("1.0", content)
    
    def get_category_widget(self, category: str) -> CategoryCard:
        """Get category widget by key."""
        return self.category_widgets.get(category)


class PromptPage(BasePage):
    """Prompt generation page."""
    
    def __init__(
        self,
        parent,
        on_generate: Callable,
        on_copy: Callable,
        on_save: Callable,
        on_send: Callable,
        on_clear: Callable
    ):
        """Initialize prompt page."""
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=2)
        
        # Title
        title = ctk.CTkLabel(
            self,
            text="Geração de Prompt",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.grid(row=0, column=0, sticky="w", pady=(0, 15))
        
        # Instructions frame
        instructions_frame = ctk.CTkFrame(self)
        instructions_frame.grid(row=1, column=0, sticky="nsew", pady=(0, 10))
        instructions_frame.grid_rowconfigure(1, weight=1)
        instructions_frame.grid_columnconfigure(0, weight=1)
        
        inst_label = ctk.CTkLabel(
            instructions_frame,
            text="💭 O que você quer que o Claude faça?",
            font=ctk.CTkFont(size=15, weight="bold")
        )
        inst_label.grid(row=0, column=0, sticky="w", padx=15, pady=10)
        
        self.user_instructions = ctk.CTkTextbox(
            instructions_frame,
            font=ctk.CTkFont(size=13),
            wrap="word"
        )
        self.user_instructions.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 15))
        self.user_instructions.insert(
            "1.0",
            "Exemplo: Analise este código e sugira melhorias de performance e segurança."
        )
        
        # Button frame
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.grid(row=2, column=0, sticky="ew", pady=10)
        
        ActionButton(
            btn_frame,
            text="🔄 Gerar Preview",
            command=on_generate,
            variant="primary"
        ).pack(side="left", padx=5)
        
        ActionButton(
            btn_frame,
            text="📋 Copiar",
            command=on_copy,
            variant="secondary"
        ).pack(side="left", padx=5)
        
        ActionButton(
            btn_frame,
            text="💾 Salvar",
            command=on_save,
            variant="secondary"
        ).pack(side="left", padx=5)
        
        ActionButton(
            btn_frame,
            text="🗑️ Limpar",
            command=on_clear,
            variant="danger"
        ).pack(side="right", padx=5)
        
        self.send_btn = ActionButton(
            btn_frame,
            text="🚀 Enviar para Claude",
            command=on_send,
            variant="success"
        )
        self.send_btn.pack(side="right", padx=5)
        
        # Preview frame
        preview_frame = ctk.CTkFrame(self)
        preview_frame.grid(row=3, column=0, sticky="nsew")
        preview_frame.grid_rowconfigure(1, weight=1)
        preview_frame.grid_columnconfigure(0, weight=1)
        
        preview_label = ctk.CTkLabel(
            preview_frame,
            text="👁️ Preview do Prompt",
            font=ctk.CTkFont(size=15, weight="bold")
        )
        preview_label.grid(row=0, column=0, sticky="w", padx=15, pady=10)
        
        self.prompt_preview = ctk.CTkTextbox(
            preview_frame,
            font=ctk.CTkFont(size=12, family="Courier"),
            wrap="word"
        )
        self.prompt_preview.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 15))
        
        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(self, mode="indeterminate")
        self.progress_bar.grid(row=4, column=0, sticky="ew", pady=(10, 0))
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


class ResultPage(BasePage):
    """Results display page."""
    
    def __init__(
        self,
        parent,
        on_copy: Callable,
        on_save: Callable,
        on_apply: Callable
    ):
        """Initialize result page."""
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        
        # Header
        header = PageHeader(self, "Resposta do Claude")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 15))
        
        header.add_button("📋 Copiar", on_copy)
        header.add_button("💾 Salvar", on_save, fg_color="transparent", border_width=2)
        header.add_button("🔄 Aplicar", on_apply, fg_color="#10b981", hover_color="#059669")
        
        # Result frame
        result_frame = ctk.CTkFrame(self)
        result_frame.grid(row=1, column=0, sticky="nsew")
        result_frame.grid_rowconfigure(0, weight=1)
        result_frame.grid_columnconfigure(0, weight=1)
        
        self.result_text = ctk.CTkTextbox(
            result_frame,
            font=ctk.CTkFont(size=13),
            wrap="word"
        )
        self.result_text.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)
    
    def get_result(self) -> str:
        """Get result text."""
        return self.result_text.get("1.0", "end")
    
    def set_result(self, text: str):
        """Set result text."""
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", text)


class DocsPage(BasePage):
    """Documentation tools page."""
    
    def __init__(
        self,
        parent,
        on_docstrings: Callable,
        on_readme: Callable,
        on_api_docs: Callable,
        on_analyze: Callable
    ):
        """Initialize docs page."""
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        
        # Title
        title = ctk.CTkLabel(
            self,
            text="Ferramentas de Documentação",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.grid(row=0, column=0, sticky="w", pady=(0, 20))
        
        # Tools frame
        tools_frame = ctk.CTkScrollableFrame(self)
        tools_frame.grid(row=1, column=0, sticky="nsew")
        
        # Tool cards
        tools = [
            ("📝", "Gerar Docstrings", "Adiciona docstrings detalhadas a funções e classes", on_docstrings),
            ("📄", "Gerar README.md", "Cria um README.md completo para o projeto", on_readme),
            ("🔌", "Documentação de API", "Gera docs completas dos endpoints da API", on_api_docs),
            ("🔍", "Análise de Código", "Análise profunda de qualidade e segurança", on_analyze),
        ]
        
        for icon, title_text, desc, command in tools:
            card = ToolCard(tools_frame, icon, title_text, desc, command)
            card.pack(fill="x", padx=10, pady=10)
