"""Prompt building and formatting module."""

from pathlib import Path
from typing import List, Dict
from .models import CodeSegment
from .config import CategoryConfig


class PromptBuilder:
    """Builds formatted prompts for Claude API."""
    
    @staticmethod
    def build_prompt(user_request: str, code_segments: List[CodeSegment]) -> str:
        """
        Build a formatted prompt from user request and code segments.
        
        Args:
            user_request: The user's instructions
            code_segments: List of code segments to include
            
        Returns:
            Formatted prompt string
        """
        prompt_parts = []
        
        # Header
        prompt_parts.append("# Análise e Modificação de Código\n")
        prompt_parts.append(f"\n## Solicitação do Usuário:\n{user_request}\n")
        
        # Organize by category
        categories: Dict[str, List[CodeSegment]] = {}
        for segment in code_segments:
            if segment.selected:
                if segment.category not in categories:
                    categories[segment.category] = []
                categories[segment.category].append(segment)
        
        if not categories:
            return "Nenhum código selecionado para análise."
        
        # Add code structure
        prompt_parts.append("\n## Estrutura do Código:\n")
        
        for category, segments in categories.items():
            category_name = CategoryConfig.get_display_name(category)
            prompt_parts.append(f"\n### {category_name}:\n")
            
            for segment in segments:
                filename = Path(segment.path).name
                prompt_parts.append(f"\n#### Arquivo: `{filename}`\n")
                prompt_parts.append(f"```\n{segment.content}\n```\n")
        
        # Footer instructions
        prompt_parts.append("\n## Instruções:\n")
        prompt_parts.append("Analise o código fornecido e forneça uma resposta clara, ")
        prompt_parts.append("estruturada e detalhada conforme solicitado.\n")
        
        return "".join(prompt_parts)
    
    @staticmethod
    def build_docstring_prompt(code_segments: List[CodeSegment]) -> str:
        """Build prompt for generating docstrings."""
        return PromptBuilder.build_prompt(
            "Gere docstrings detalhadas no formato apropriado para cada função, "
            "classe e módulo no código. Use o formato padrão da linguagem (PEP 257 "
            "para Python, JSDoc para JavaScript, etc.).",
            code_segments
        )
    
    @staticmethod
    def build_readme_prompt(code_segments: List[CodeSegment]) -> str:
        """Build prompt for generating README."""
        return PromptBuilder.build_prompt(
            "Gere um README.md completo e profissional incluindo:\n"
            "- Descrição clara do projeto\n"
            "- Funcionalidades principais\n"
            "- Requisitos e dependências\n"
            "- Instruções de instalação\n"
            "- Guia de uso com exemplos\n"
            "- Estrutura do projeto\n"
            "- Tecnologias utilizadas\n"
            "- Como contribuir\n"
            "- Licença",
            code_segments
        )
    
    @staticmethod
    def build_api_docs_prompt(code_segments: List[CodeSegment]) -> str:
        """Build prompt for generating API documentation."""
        return PromptBuilder.build_prompt(
            "Gere documentação completa de API incluindo:\n"
            "- Lista de todos os endpoints disponíveis\n"
            "- Métodos HTTP suportados\n"
            "- Parâmetros (query, body, headers)\n"
            "- Formatos de requisição e resposta\n"
            "- Códigos de status HTTP\n"
            "- Exemplos práticos de uso (curl, JavaScript, Python)\n"
            "- Requisitos de autenticação\n"
            "- Rate limiting e restrições",
            code_segments
        )
    
    @staticmethod
    def build_analysis_prompt(code_segments: List[CodeSegment]) -> str:
        """Build prompt for code analysis."""
        return PromptBuilder.build_prompt(
            "Realize uma análise completa e profunda do código incluindo:\n"
            "- Qualidade geral e organização\n"
            "- Aderência a boas práticas e padrões\n"
            "- Possíveis bugs e vulnerabilidades\n"
            "- Oportunidades de otimização de performance\n"
            "- Questões de segurança\n"
            "- Manutenibilidade e escalabilidade\n"
            "- Cobertura de testes\n"
            "- Qualidade da documentação\n"
            "- Sugestões de refatoração\n"
            "- Pontos fortes e fracos",
            code_segments
        )
    
    @staticmethod
    def get_prompt_stats(prompt: str) -> Dict[str, int]:
        """
        Get statistics about a prompt.
        
        Args:
            prompt: The prompt text
            
        Returns:
            Dictionary with statistics
        """
        return {
            'characters': len(prompt),
            'lines': prompt.count('\n') + 1,
            'words': len(prompt.split()),
            'estimated_tokens': len(prompt) // 4  # Rough estimate
        }
