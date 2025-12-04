"""Main application module."""

import customtkinter as ctk
from tkinter import filedialog, messagebox
from pathlib import Path
import threading
from typing import Optional

from .config import config, theme, CategoryConfig
from .api_client import ClaudeAPIClient
from .file_manager import FileManager
from .prompt_builder import PromptBuilder
from .ui.pages import FilesPage, DocsPage
from .ui.modern_pages import ModernLoginPage, ModernPromptPage, ModernResultPage
from .ui.modern_widgets import ModernStatusBadge, ModernDivider


class ClaudePromptGeneratorApp:
    """Main application class."""
    
    def __init__(self):
        """Initialize the application."""
        # Setup window
        self.root = ctk.CTk()
        self.root.title(config.WINDOW_TITLE)
        self.root.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.root.minsize(config.WINDOW_MIN_WIDTH, config.WINDOW_MIN_HEIGHT)
        
        # Apply modern theme
        ctk.set_appearance_mode(config.APPEARANCE_MODE)
        ctk.set_default_color_theme(config.COLOR_THEME)
        
        # Configure window background
        self.root.configure(fg_color=theme.BG_PRIMARY)
        
        # Initialize components
        self.api_client = ClaudeAPIClient()
        self.file_manager = FileManager()
        
        # Setup UI
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface."""
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        self.setup_sidebar()
        self.setup_main_content()
    
    def setup_sidebar(self):
        """Setup the sidebar navigation."""
        self.sidebar = ctk.CTkFrame(
            self.root,
            width=config.SIDEBAR_WIDTH,
            corner_radius=0,
            fg_color=theme.BG_SECONDARY,
            border_width=0
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        
        # Logo/Header section
        header_frame = ctk.CTkFrame(self.sidebar, fg_color=theme.BG_SECONDARY)
        header_frame.pack(pady=(config.SPACING_XL, config.SPACING_MD), padx=config.SPACING_LG)
        
        # Icon
        icon_label = ctk.CTkLabel(
            header_frame,
            text="🤖",
            font=ctk.CTkFont(size=48)
        )
        icon_label.pack()
        
        # Title
        title_label = ctk.CTkLabel(
            header_frame,
            text="CODEX",
            font=ctk.CTkFont(
                family=config.FONT_FAMILY,
                size=config.FONT_SIZE_TITLE,
                weight="bold"
            ),
            text_color=theme.TEXT_PRIMARY
        )
        title_label.pack(pady=(config.SPACING_SM, 0))
        
        # Version badge
        from .config import APP_VERSION
        version_badge = ctk.CTkLabel(
            header_frame,
            text=f"v{APP_VERSION}",
            font=ctk.CTkFont(
                family=config.FONT_FAMILY,
                size=config.FONT_SIZE_SMALL,
                weight="bold"
            ),
            text_color=theme.PRIMARY,
            fg_color=theme.BG_TERTIARY,
            corner_radius=config.RADIUS_SM,
            padx=10,
            pady=4
        )
        version_badge.pack(pady=(config.SPACING_SM, 0))
        
        # Divider
        ModernDivider(self.sidebar).pack(fill="x", padx=config.SPACING_LG, pady=config.SPACING_MD)
        
        # Navigation
        nav_container = ctk.CTkFrame(self.sidebar, fg_color=theme.BG_SECONDARY)
        nav_container.pack(fill="both", expand=True, padx=15, pady=10)
        
        self.nav_buttons = {}
        nav_items = [
            ("🔐 Login", "login"),
            ("📁 Arquivos", "files"),
            ("✏️ Prompt", "prompt"),
            ("💬 Resultado", "result"),
            ("📚 Docs", "docs")
        ]
        
        for text, key in nav_items:
            btn = ctk.CTkButton(
                nav_container,
                text=text,
                command=lambda k=key: self.show_page(k),
                height=50,
                corner_radius=config.RADIUS_MD,
                font=ctk.CTkFont(
                    family=config.FONT_FAMILY,
                    size=config.FONT_SIZE_NORMAL,
                    weight="bold"
                ),
                fg_color=theme.BG_SECONDARY,
                text_color=theme.TEXT_SECONDARY,
                hover_color=theme.BG_TERTIARY,
                anchor="w",
                border_spacing=10
            )
            btn.pack(fill="x", pady=config.SPACING_XS)
            self.nav_buttons[key] = btn
        
        # Footer
        ModernDivider(self.sidebar).pack(fill="x", padx=config.SPACING_LG, pady=config.SPACING_MD, side="bottom")
        
        footer_frame = ctk.CTkFrame(self.sidebar, fg_color=theme.BG_SECONDARY)
        footer_frame.pack(side="bottom", fill="x", padx=config.SPACING_LG, pady=config.SPACING_LG)
        
        # Connection status
        self.connection_indicator = ModernStatusBadge(
            footer_frame,
            text="Desconectado",
            status="idle"
        )
        self.connection_indicator.pack(pady=(0, config.SPACING_SM))
        
        # Status message
        self.status_label = ctk.CTkLabel(
            footer_frame,
            text="Pronto para começar",
            font=ctk.CTkFont(
                family=config.FONT_FAMILY,
                size=config.FONT_SIZE_SMALL
            ),
            text_color=theme.TEXT_MUTED,
            wraplength=260,
            justify="left"
        )
        self.status_label.pack(anchor="w")
    
    def setup_main_content(self):
        """Setup the main content area."""
        self.main_container = ctk.CTkFrame(
            self.root,
            corner_radius=0,
            fg_color=theme.BG_PRIMARY
        )
        self.main_container.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=config.SPACING_LG,
            pady=config.SPACING_LG
        )
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)
        
        # Create pages
        self.pages = {}
        
        self.pages["login"] = ModernLoginPage(
            self.main_container,
            on_login=self.handle_login,
            on_test=self.handle_test_connection
        )
        
        self.pages["files"] = FilesPage(
            self.main_container,
            on_open=self.handle_open_repository,
            on_refresh=self.handle_refresh_files,
            on_add=self.handle_add_to_category,
            on_remove=self.handle_remove_from_category
        )
        
        self.pages["prompt"] = ModernPromptPage(
            self.main_container,
            on_generate=self.handle_generate_preview,
            on_copy=self.handle_copy_prompt,
            on_save=self.handle_save_prompt,
            on_send=self.handle_send_to_claude,
            on_clear=self.handle_clear_prompt
        )
        
        self.pages["result"] = ModernResultPage(
            self.main_container,
            on_copy=self.handle_copy_result,
            on_save=self.handle_save_result,
            on_apply=self.handle_apply_changes
        )
        
        self.pages["docs"] = DocsPage(
            self.main_container,
            on_docstrings=self.handle_generate_docstrings,
            on_readme=self.handle_generate_readme,
            on_api_docs=self.handle_generate_api_docs,
            on_analyze=self.handle_analyze_code
        )
        
        # Show initial page
        self.show_page("login")
    
    def show_page(self, page_name: str):
        """Show a specific page."""
        for name, page in self.pages.items():
            if name == page_name:
                page.grid(row=0, column=0, sticky="nsew")
            else:
                page.grid_forget()
        
        # Update navigation buttons with modern styling
        for name, btn in self.nav_buttons.items():
            if name == page_name:
                btn.configure(
                    fg_color=theme.PRIMARY,
                    text_color=theme.TEXT_PRIMARY
                )
            else:
                btn.configure(
                    fg_color="transparent",
                    text_color=theme.TEXT_SECONDARY
                )
    
    def update_status(self, message: str):
        """Update status message."""
        self.status_label.configure(text=message)
    
    # Login handlers
    def handle_login(self):
        """Handle login button click."""
        login_page = self.pages["login"]
        api_key = login_page.get_api_key()
        
        if not api_key:
            messagebox.showerror("Erro", "Por favor, insira sua API Key")
            return
        
        login_page.set_loading(True)
        self.root.update()
        
        response = self.api_client.connect(api_key)
        
        login_page.set_loading(False)
        
        if response.success:
            self.connection_indicator.set_status("connected", "Conectado")
            self.update_status("Conectado ao Claude API")
            messagebox.showinfo("Sucesso", "Conectado com sucesso ao Claude API!")
            self.show_page("files")
        else:
            self.connection_indicator.set_status("error", "Erro de conexão")
            messagebox.showerror("Erro de Conexão", f"Falha ao conectar:\n{response.error}")
    
    def handle_test_connection(self):
        """Handle test connection button click."""
        login_page = self.pages["login"]
        if not login_page.get_api_key():
            messagebox.showwarning("Aviso", "Insira uma API Key primeiro")
            return
        self.handle_login()
    
    # File handlers
    def handle_open_repository(self):
        """Handle open repository button click."""
        folder = filedialog.askdirectory(title="Selecione o Repositório")
        
        if folder:
            if self.file_manager.set_project_path(folder):
                files_page = self.pages["files"]
                files_page.set_project_path(folder)
                
                tree = self.file_manager.scan_directory()
                files_page.set_files_content(tree)
                
                self.update_status(f"Projeto carregado: {Path(folder).name}")
    
    def handle_refresh_files(self):
        """Handle refresh files button click."""
        if self.file_manager.project_path:
            files_page = self.pages["files"]
            tree = self.file_manager.scan_directory()
            files_page.set_files_content(tree)
            self.update_status("Arquivos atualizados")
    
    def handle_add_to_category(self, category: str):
        """Handle add to category button click."""
        if not self.file_manager.project_path:
            messagebox.showwarning("Aviso", "Abra um repositório primeiro")
            return
        
        files = filedialog.askopenfilenames(
            initialdir=self.file_manager.project_path,
            title="Selecione arquivos"
        )
        
        if files:
            files_page = self.pages["files"]
            widget = files_page.get_category_widget(category)
            
            for filepath in files:
                if self.file_manager.add_file(filepath, category):
                    filename = Path(filepath).name
                    widget.add_file(filename)
            
            count = self.file_manager.get_segment_count()
            self.update_status(f"{len(files)} arquivo(s) adicionado(s). Total: {count}")
    
    def handle_remove_from_category(self, category: str):
        """Handle remove from category button click."""
        files_page = self.pages["files"]
        widget = files_page.get_category_widget(category)
        widget.clear()
        
        removed = self.file_manager.remove_files_by_category(category)
        count = self.file_manager.get_segment_count()
        self.update_status(f"{removed} arquivo(s) removido(s). Total: {count}")
    
    # Prompt handlers
    def handle_generate_preview(self):
        """Handle generate preview button click."""
        if not self.file_manager.code_segments:
            messagebox.showwarning("Aviso", "Adicione arquivos às categorias primeiro")
            return
        
        prompt_page = self.pages["prompt"]
        user_request = prompt_page.get_user_instructions()
        
        prompt = PromptBuilder.build_prompt(
            user_request,
            self.file_manager.code_segments
        )
        
        prompt_page.set_prompt_preview(prompt)
        
        stats = PromptBuilder.get_prompt_stats(prompt)
        self.update_status(
            f"Preview gerado: {stats['characters']} chars, "
            f"~{stats['estimated_tokens']} tokens"
        )
    
    def handle_copy_prompt(self):
        """Handle copy prompt button click."""
        prompt_page = self.pages["prompt"]
        prompt = prompt_page.get_prompt_preview()
        
        if prompt:
            self.root.clipboard_clear()
            self.root.clipboard_append(prompt)
            self.update_status("Prompt copiado para área de transferência")
        else:
            messagebox.showwarning("Aviso", "Gere um preview primeiro")
    
    def handle_save_prompt(self):
        """Handle save prompt button click."""
        prompt_page = self.pages["prompt"]
        prompt = prompt_page.get_prompt_preview()
        
        if not prompt:
            messagebox.showwarning("Aviso", "Gere um preview primeiro")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Text files", "*.txt"),
                ("Markdown", "*.md"),
                ("All files", "*.*")
            ]
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(prompt)
                self.update_status(f"Prompt salvo: {Path(filename).name}")
                messagebox.showinfo("Sucesso", "Prompt salvo com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar: {e}")
    
    def handle_clear_prompt(self):
        """Handle clear prompt button click."""
        prompt_page = self.pages["prompt"]
        prompt_page.clear_all()
        self.update_status("Prompt limpo")
    
    def handle_send_to_claude(self):
        """Handle send to Claude button click."""
        if not self.api_client.is_connected():
            messagebox.showerror("Erro", "Faça login primeiro!")
            return
        
        if not self.file_manager.code_segments:
            messagebox.showwarning("Aviso", "Adicione código primeiro")
            return
        
        prompt_page = self.pages["prompt"]
        prompt = prompt_page.get_prompt_preview()
        
        if not prompt:
            self.handle_generate_preview()
            prompt = prompt_page.get_prompt_preview()
        
        if not prompt:
            messagebox.showerror("Erro", "Não foi possível gerar o prompt")
            return
        
        # Show progress and switch to result page
        prompt_page.show_progress(True)
        self.update_status("Enviando para Claude...")
        self.show_page("result")
        
        # Send in background thread
        thread = threading.Thread(
            target=self._send_to_claude_thread,
            args=(prompt,)
        )
        thread.daemon = True
        thread.start()
    
    def _send_to_claude_thread(self, prompt: str):
        """Send message to Claude in background thread."""
        response = self.api_client.send_message(prompt)
        self.root.after(0, self._handle_claude_response, response)
    
    def _handle_claude_response(self, response):
        """Handle Claude API response."""
        prompt_page = self.pages["prompt"]
        prompt_page.show_progress(False)
        
        if response.success:
            result_page = self.pages["result"]
            result_page.set_result(response.content)
            
            tokens = response.tokens_used or 0
            self.update_status(f"Resposta recebida ({tokens} tokens)")
        else:
            self.update_status(f"Erro: {response.error}")
            messagebox.showerror(
                "Erro",
                f"Erro ao comunicar com Claude:\n{response.error}"
            )
    
    # Result handlers
    def handle_copy_result(self):
        """Handle copy result button click."""
        result_page = self.pages["result"]
        result = result_page.get_result()
        
        if result:
            self.root.clipboard_clear()
            self.root.clipboard_append(result)
            self.update_status("Resultado copiado para área de transferência")
    
    def handle_save_result(self):
        """Handle save result button click."""
        result_page = self.pages["result"]
        result = result_page.get_result()
        
        if not result.strip():
            messagebox.showwarning("Aviso", "Nenhum resultado para salvar")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".md",
            filetypes=[
                ("Markdown", "*.md"),
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(result)
                self.update_status(f"Resultado salvo: {Path(filename).name}")
                messagebox.showinfo("Sucesso", "Resultado salvo com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar: {e}")
    
    def handle_apply_changes(self):
        """Handle apply changes button click."""
        result = messagebox.askyesno(
            "Aplicar Mudanças",
            "Esta função permite revisar e aplicar mudanças sugeridas.\n\n"
            "Por segurança, revise manualmente as sugestões.\n\n"
            "Deseja continuar?"
        )
        
        if result:
            self._open_apply_changes_window()
    
    def _open_apply_changes_window(self):
        """Open apply changes review window."""
        result_page = self.pages["result"]
        result = result_page.get_result()
        
        window = ctk.CTkToplevel(self.root)
        window.title("Aplicar Mudanças")
        window.geometry("900x700")
        
        title = ctk.CTkLabel(
            window,
            text="Revisão de Mudanças Sugeridas",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title.pack(pady=20)
        
        text = ctk.CTkTextbox(window, font=ctk.CTkFont(size=12))
        text.pack(fill="both", expand=True, padx=20, pady=(0, 10))
        text.insert("1.0", result)
        
        warning = ctk.CTkLabel(
            window,
            text="⚠️ Revise cuidadosamente antes de aplicar!",
            font=ctk.CTkFont(size=13),
            text_color="#f59e0b"
        )
        warning.pack(pady=10)
        
        close_btn = ctk.CTkButton(
            window,
            text="Fechar",
            command=window.destroy,
            height=40,
            font=ctk.CTkFont(size=14)
        )
        close_btn.pack(pady=20)
    
    # Documentation tool handlers
    def handle_generate_docstrings(self):
        """Handle generate docstrings tool."""
        if not self._check_prerequisites():
            return
        
        prompt_page = self.pages["prompt"]
        prompt_page.set_user_instructions(
            "Gere docstrings detalhadas no formato apropriado para cada função, "
            "classe e módulo no código. Use o formato padrão da linguagem."
        )
        
        self.show_page("prompt")
        self.handle_generate_preview()
    
    def handle_generate_readme(self):
        """Handle generate README tool."""
        if not self._check_prerequisites():
            return
        
        prompt_page = self.pages["prompt"]
        prompt_page.set_user_instructions(
            "Gere um README.md completo incluindo:\n"
            "- Descrição do projeto\n"
            "- Funcionalidades principais\n"
            "- Instalação e uso\n"
            "- Estrutura do projeto\n"
            "- Tecnologias utilizadas\n"
            "- Contribuição e licença"
        )
        
        self.show_page("prompt")
        self.handle_generate_preview()
    
    def handle_generate_api_docs(self):
        """Handle generate API docs tool."""
        if not self._check_prerequisites():
            return
        
        prompt_page = self.pages["prompt"]
        prompt_page.set_user_instructions(
            "Gere documentação completa de API incluindo:\n"
            "- Endpoints disponíveis\n"
            "- Métodos HTTP\n"
            "- Parâmetros e formatos\n"
            "- Códigos de status\n"
            "- Exemplos de uso\n"
            "- Autenticação necessária"
        )
        
        self.show_page("prompt")
        self.handle_generate_preview()
    
    def handle_analyze_code(self):
        """Handle analyze code tool."""
        if not self._check_prerequisites():
            return
        
        prompt_page = self.pages["prompt"]
        prompt_page.set_user_instructions(
            "Análise completa do código incluindo:\n"
            "- Qualidade e organização\n"
            "- Boas práticas e padrões\n"
            "- Possíveis bugs\n"
            "- Melhorias de performance\n"
            "- Questões de segurança\n"
            "- Manutenibilidade e testes\n"
            "- Documentação"
        )
        
        self.show_page("prompt")
        self.handle_generate_preview()
    
    def _check_prerequisites(self) -> bool:
        """Check if prerequisites are met for documentation tools."""
        if not self.api_client.is_connected():
            messagebox.showerror("Erro", "Faça login primeiro!")
            return False
        
        if not self.file_manager.code_segments:
            messagebox.showwarning("Aviso", "Adicione código primeiro")
            return False
        
        return True
    
    def run(self):
        """Run the application."""
        self.root.mainloop()
