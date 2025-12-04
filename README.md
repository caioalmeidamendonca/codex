# 🤖 CODEX

<div align="center">

![Version](https://img.shields.io/badge/version-2.1.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

**Uma ferramenta profissional e modular para gerar prompts otimizados para Claude AI**

[Características](#-características) • [Instalação](#-instalação) • [Uso](#-uso) • [Arquitetura](#-arquitetura) • [Contribuir](#-contribuir)

</div>

---

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Características](#-características)
- [Requisitos](#-requisitos)
- [Instalação](#-instalação)
- [Uso](#-uso)
- [Arquitetura](#-arquitetura)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Configuração](#-configuração)
- [Desenvolvimento](#-desenvolvimento)
- [Solução de Problemas](#-solução-de-problemas)
- [Contribuir](#-contribuir)
- [Licença](#-licença)

---

## 🎯 Visão Geral

O **CODEX** é uma aplicação desktop moderna e intuitiva que facilita a criação de prompts estruturados e otimizados para a API do Claude AI. Com uma interface gráfica elegante e funcionalidades avançadas, permite organizar código-fonte por categorias, gerar documentação automaticamente e interagir diretamente com o Claude.

### ✨ Novidades da Versão 2.1 (Modern Edition)

- 🎨 **Design Moderno**: Interface completamente redesenhada com tema escuro profissional
- 🌈 **Sistema de Cores Avançado**: Paleta de cores moderna com gradientes e transições suaves
- 📱 **Totalmente Responsivo**: Layout adaptável com tamanhos mínimos e máximos
- ✨ **Animações Fluidas**: Efeitos hover, transições e feedback visual aprimorado
- 🎯 **Widgets Modernos**: Componentes UI redesenhados (cards, buttons, inputs, badges)
- 🏗️ **Arquitetura Modular**: Código completamente refatorado com separação clara de responsabilidades
- 🚀 **Setup Automático**: Instalação com um único clique
- 📦 **Gerenciamento Aprimorado**: Sistema de arquivos e categorias otimizado
- 🔧 **Configuração Centralizada**: Fácil customização e manutenção
- 📚 **Documentação Completa**: Código bem documentado e README detalhado

---

## 🌟 Características

### Interface Gráfica Moderna
- 🎨 Tema escuro elegante com CustomTkinter
- 📱 Layout responsivo e intuitivo
- 🔄 Navegação fluida entre páginas
- 💫 Indicadores visuais de status

### Gerenciamento de Código
- 📁 Explorador de arquivos com visualização em árvore
- 🏷️ Sistema de categorização inteligente (10 categorias)
- 📄 Suporte para múltiplas linguagens de programação
- 🔍 Filtragem automática de arquivos relevantes

### Integração com Claude AI
- 🔐 Autenticação segura com API Key
- 💬 Envio direto de prompts para Claude
- ⚡ Processamento assíncrono (não trava a interface)
- 📊 Estatísticas de tokens e caracteres

### Ferramentas de Documentação
- 📝 Geração automática de docstrings
- 📄 Criação de README.md profissional
- 🔌 Documentação de APIs e endpoints
- 🔍 Análise profunda de código

### Funcionalidades Avançadas
- 📋 Cópia rápida para área de transferência
- 💾 Salvamento de prompts e resultados
- 🔄 Preview em tempo real
- ⚙️ Configuração personalizável

---

## 💻 Requisitos

### Sistema Operacional
- Windows 10/11
- macOS 10.14+
- Linux (Ubuntu 20.04+, Fedora, etc.)

### Software
- **Python 3.8 ou superior**
- **pip** (gerenciador de pacotes Python)

### Dependências Python
- `anthropic >= 0.40.0` - Cliente oficial da API Claude
- `customtkinter >= 5.2.0` - Framework de interface gráfica moderna
- `Pillow >= 10.0.0` - Processamento de imagens

### Requisitos Adicionais
- **API Key do Claude** (obtenha em: https://console.anthropic.com/)
- Conexão com internet para comunicação com a API

---

## 🚀 Instalação

### Método 1: Setup Automático (Recomendado) ⭐

1. **Clone ou baixe o repositório**
   ```bash
   git clone https://github.com/seu-usuario/claude-prompt-generator.git
   cd claude-prompt-generator
   ```

2. **Execute o setup automático**
   
   **Windows:**
   ```bash
   setup.bat
   ```
   
   **Linux/macOS:**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Pronto!** O setup irá:
   - ✓ Verificar a instalação do Python
   - ✓ Atualizar o pip
   - ✓ Instalar todas as dependências
   - ✓ Oferecer iniciar o aplicativo

### Método 2: Instalação Manual

1. **Verifique o Python**
   ```bash
   python --version
   # Deve mostrar Python 3.8 ou superior
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o aplicativo**
   ```bash
   python main.py
   ```

---

## 📖 Uso

### Iniciando o Aplicativo

**Windows:**
```bash
start.bat
```

**Linux/macOS:**
```bash
python main.py
```

### Fluxo de Trabalho

#### 1️⃣ Configuração Inicial

1. Na tela de **Login**, insira sua API Key do Claude
2. Clique em **"Testar Conexão"** para verificar
3. Clique em **"Conectar"** para prosseguir

> 💡 **Dica:** Obtenha sua API Key em https://console.anthropic.com/

#### 2️⃣ Gerenciamento de Arquivos

1. Navegue até **"📁 Arquivos"**
2. Clique em **"📂 Abrir Repositório"**
3. Selecione a pasta do seu projeto
4. Visualize a estrutura de arquivos na árvore

#### 3️⃣ Organização por Categorias

1. Selecione uma categoria (Backend, Frontend, etc.)
2. Clique em **"← Adicionar"**
3. Escolha os arquivos relevantes
4. Repita para outras categorias conforme necessário

**Categorias Disponíveis:**
- 🗄️ Banco de Dados
- ⚙️ Backend
- 🎨 Frontend
- 📝 Modelos
- 🔧 Utilitários
- 🧪 Testes
- 📋 Config
- 📚 Docs
- 🔌 API
- 🎯 Outro

#### 4️⃣ Geração de Prompt

1. Vá para **"✏️ Prompt"**
2. Descreva o que deseja no campo de instruções
3. Clique em **"🔄 Gerar Preview"**
4. Revise o prompt gerado

**Exemplos de Instruções:**
- "Analise este código e sugira melhorias de performance"
- "Refatore este código seguindo princípios SOLID"
- "Identifique possíveis vulnerabilidades de segurança"
- "Adicione tratamento de erros robusto"

#### 5️⃣ Envio para Claude

1. Clique em **"🚀 Enviar para Claude"**
2. Aguarde o processamento (barra de progresso)
3. Visualize a resposta na página **"💬 Resultado"**

#### 6️⃣ Gerenciamento de Resultados

- **📋 Copiar**: Copia o resultado para área de transferência
- **💾 Salvar**: Salva em arquivo (.md ou .txt)
- **🔄 Aplicar**: Abre janela de revisão para aplicar mudanças

### Ferramentas de Documentação

Acesse **"📚 Docs"** para ferramentas especializadas:

#### 📝 Gerar Docstrings
Adiciona documentação detalhada a funções e classes

#### 📄 Gerar README.md
Cria um README completo para seu projeto

#### 🔌 Documentação de API
Gera documentação de endpoints e APIs

#### 🔍 Análise de Código
Análise profunda de qualidade, segurança e performance

---

## 🏗️ Arquitetura

### Visão Geral

O projeto segue uma arquitetura modular com separação clara de responsabilidades:

```
┌─────────────────────────────────────────────┐
│              main.py (Entry Point)          │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│           src/app.py (Controller)           │
│  ┌──────────────────────────────────────┐   │
│  │  - Gerencia fluxo da aplicação      │   │
│  │  - Coordena componentes              │   │
│  │  - Trata eventos da UI               │   │
│  └──────────────────────────────────────┘   │
└───┬─────────────┬─────────────┬─────────────┘
    │             │             │
    ▼             ▼             ▼
┌─────────┐  ┌─────────┐  ┌──────────┐
│   UI    │  │  Logic  │  │  Config  │
│ Package │  │ Modules │  │  Module  │
└─────────┘  └─────────┘  └──────────┘
```

### Módulos Principais

#### 📦 `src/config.py`
- Configurações centralizadas
- Constantes da aplicação
- Categorias de código

#### 📦 `src/models.py`
- Modelos de dados (CodeSegment, APIResponse)
- Estruturas de dados tipadas

#### 📦 `src/api_client.py`
- Cliente da API Claude
- Gerenciamento de conexão
- Envio e recebimento de mensagens

#### 📦 `src/file_manager.py`
- Escaneamento de diretórios
- Gerenciamento de arquivos
- Organização por categorias

#### 📦 `src/prompt_builder.py`
- Construção de prompts formatados
- Templates especializados
- Estatísticas de prompts

#### 📦 `src/ui/widgets.py`
- Componentes reutilizáveis
- Widgets customizados
- Elementos visuais

#### 📦 `src/ui/pages.py`
- Páginas da aplicação
- Layouts e estruturas
- Interação com usuário

#### 📦 `src/app.py`
- Controlador principal
- Coordenação de componentes
- Gerenciamento de eventos

### Princípios de Design

- **Separação de Responsabilidades**: Cada módulo tem uma função específica
- **Baixo Acoplamento**: Módulos independentes e intercambiáveis
- **Alta Coesão**: Funcionalidades relacionadas agrupadas
- **Reutilização**: Componentes e widgets reutilizáveis
- **Testabilidade**: Código estruturado para testes
- **Manutenibilidade**: Código limpo e bem documentado

---

## 📁 Estrutura do Projeto

```
claude-prompt-generator/
│
├── 📄 main.py                      # Ponto de entrada da aplicação
├── 📄 requirements.txt             # Dependências Python
├── 📄 README.md                    # Documentação principal
│
├── 🔧 setup.bat                    # Setup automático (Windows)
├── 🔧 start.bat                    # Iniciar aplicação (Windows)
│
├── 📦 src/                         # Código-fonte principal
│   ├── 📄 __init__.py
│   ├── 📄 config.py                # Configurações
│   ├── 📄 models.py                # Modelos de dados
│   ├── 📄 api_client.py            # Cliente API Claude
│   ├── 📄 file_manager.py          # Gerenciador de arquivos
│   ├── 📄 prompt_builder.py        # Construtor de prompts
│   ├── 📄 app.py                   # Aplicação principal
│   │
│   └── 📦 ui/                      # Componentes de interface
│       ├── 📄 __init__.py
│       ├── 📄 widgets.py           # Widgets reutilizáveis
│       └── 📄 pages.py             # Páginas da aplicação
│
└── 📁 [arquivos antigos]           # Mantidos para referência
    ├── prompt_generator.py         # Versão monolítica antiga
    ├── install.bat
    └── run.bat
```

### Descrição dos Arquivos

| Arquivo | Descrição | Linhas |
|---------|-----------|--------|
| `main.py` | Entry point, inicializa a aplicação | ~30 |
| `src/config.py` | Configurações e constantes | ~80 |
| `src/models.py` | Classes de dados | ~40 |
| `src/api_client.py` | Cliente API Claude | ~100 |
| `src/file_manager.py` | Gerenciamento de arquivos | ~150 |
| `src/prompt_builder.py` | Construção de prompts | ~120 |
| `src/ui/widgets.py` | Componentes UI reutilizáveis | ~200 |
| `src/ui/pages.py` | Páginas da aplicação | ~400 |
| `src/app.py` | Controlador principal | ~600 |

---

## ⚙️ Configuração

### Personalização

Edite `src/config.py` para personalizar:

```python
# Configurações da janela
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 950

# Tema
APPEARANCE_MODE = "dark"  # "light", "dark", "system"
COLOR_THEME = "blue"      # "blue", "green", "dark-blue"

# API
DEFAULT_MODEL = "claude-sonnet-4-5-20250929"
MAX_TOKENS = 8000

# Extensões de arquivo suportadas
CODE_EXTENSIONS = {'.py', '.js', '.ts', ...}

# Diretórios ignorados
IGNORE_DIRS = {'.git', 'node_modules', ...}
```

### Variáveis de Ambiente

Opcionalmente, configure:

```bash
# API Key (alternativa ao login manual)
export ANTHROPIC_API_KEY="sua-api-key"

# Modo de aparência
export CTK_APPEARANCE_MODE="dark"
```

---

## 🛠️ Desenvolvimento

### Configurando Ambiente de Desenvolvimento

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/claude-prompt-generator.git
   cd claude-prompt-generator
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Instale dependências de desenvolvimento**
   ```bash
   pip install -r requirements.txt
   pip install pytest black flake8 mypy
   ```

### Executando Testes

```bash
# Testes unitários
pytest tests/

# Cobertura
pytest --cov=src tests/

# Linting
flake8 src/
black src/ --check

# Type checking
mypy src/
```

### Contribuindo com Código

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Padrões de Código

- **PEP 8**: Siga as convenções de estilo Python
- **Type Hints**: Use anotações de tipo
- **Docstrings**: Documente funções e classes
- **Nomes Descritivos**: Use nomes claros e significativos
- **Modularidade**: Mantenha funções pequenas e focadas

---

## 🔧 Solução de Problemas

### Problema: Python não encontrado

**Solução:**
1. Instale Python 3.8+ de https://www.python.org/
2. Durante instalação, marque "Add Python to PATH"
3. Reinicie o terminal

### Problema: Erro ao instalar dependências

**Solução:**
```bash
# Atualize pip
python -m pip install --upgrade pip

# Instale individualmente
pip install anthropic
pip install customtkinter
pip install Pillow

# Se persistir, use --user
pip install --user -r requirements.txt
```

### Problema: Erro de conexão com API

**Solução:**
1. Verifique sua API Key em https://console.anthropic.com/
2. Confirme que tem créditos disponíveis
3. Verifique sua conexão com internet
4. Tente novamente após alguns minutos

### Problema: Interface não aparece

**Solução:**
```bash
# Reinstale customtkinter
pip uninstall customtkinter
pip install customtkinter --upgrade

# Verifique Pillow
pip install Pillow --upgrade
```

### Problema: Arquivos não aparecem

**Solução:**
1. Verifique se o diretório tem permissões de leitura
2. Confirme que os arquivos têm extensões suportadas
3. Verifique se não estão em pastas ignoradas (node_modules, .git, etc.)

### Logs e Debug

Para debug detalhado, execute:

```bash
python main.py --debug
```

---

## 🤝 Contribuir

Contribuições são bem-vindas! Veja como você pode ajudar:

### Formas de Contribuir

- 🐛 **Reportar Bugs**: Abra uma issue descrevendo o problema
- 💡 **Sugerir Features**: Compartilhe suas ideias
- 📝 **Melhorar Documentação**: Corrija ou expanda a documentação
- 🔧 **Contribuir com Código**: Envie pull requests
- 🌍 **Tradução**: Ajude a traduzir para outros idiomas
- ⭐ **Star o Projeto**: Mostre seu apoio!

### Diretrizes

1. Mantenha o código limpo e documentado
2. Siga os padrões de código existentes
3. Adicione testes para novas funcionalidades
4. Atualize a documentação quando necessário
5. Seja respeitoso e construtivo

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

```
MIT License

Copyright (c) 2025 CODEX

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 Contato e Suporte

- **Issues**: https://github.com/seu-usuario/claude-prompt-generator/issues
- **Discussions**: https://github.com/caioalmeidamendonca/codex
- **Email**: caioalmeidamendonca@gmail.com

---

## 🙏 Agradecimentos

- **Anthropic** - Pela incrível API do Claude
- **CustomTkinter** - Pelo framework de UI moderno
- **Comunidade Python** - Pelo suporte e ferramentas

---

## 📊 Status do Projeto

![GitHub last commit](https://img.shields.io/github/last-commit/seu-usuario/claude-prompt-generator)
![GitHub issues](https://img.shields.io/github/issues/seu-usuario/claude-prompt-generator)
![GitHub pull requests](https://img.shields.io/github/issues-pr/seu-usuario/claude-prompt-generator)

---

<div align="center">

**Feito com ❤️ e Python**

[⬆ Voltar ao topo](#-claude-prompt-generator-pro)

</div>
