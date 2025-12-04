"""Claude API client module."""

import anthropic
from typing import Optional
from .models import APIResponse
from .config import config


class ClaudeAPIClient:
    """Handles communication with Claude API."""
    
    def __init__(self):
        """Initialize the API client."""
        self.client: Optional[anthropic.Anthropic] = None
        self.api_key: str = ""
        self._connected: bool = False
    
    def connect(self, api_key: str) -> APIResponse:
        """
        Connect to Claude API with provided key.
        
        Args:
            api_key: The API key for authentication
            
        Returns:
            APIResponse with connection status
        """
        try:
            self.client = anthropic.Anthropic(api_key=api_key)
            self.api_key = api_key
            
            # Test connection
            response = self.client.messages.create(
                model=config.DEFAULT_MODEL,
                max_tokens=config.TEST_MAX_TOKENS,
                messages=[{"role": "user", "content": "test"}]
            )
            
            self._connected = True
            return APIResponse(
                success=True,
                content="Connected successfully",
                model=config.DEFAULT_MODEL
            )
            
        except Exception as e:
            self._connected = False
            return APIResponse(
                success=False,
                error=str(e)
            )
    
    def send_message(self, prompt: str, max_tokens: Optional[int] = None) -> APIResponse:
        """
        Send a message to Claude API.
        
        Args:
            prompt: The prompt to send
            max_tokens: Maximum tokens for response (default from config)
            
        Returns:
            APIResponse with the result
        """
        if not self.is_connected():
            return APIResponse(
                success=False,
                error="Not connected to API. Please login first."
            )
        
        try:
            tokens = max_tokens or config.MAX_TOKENS
            
            response = self.client.messages.create(
                model=config.DEFAULT_MODEL,
                max_tokens=tokens,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return APIResponse(
                success=True,
                content=response.content[0].text,
                model=config.DEFAULT_MODEL,
                tokens_used=response.usage.input_tokens + response.usage.output_tokens
            )
            
        except Exception as e:
            return APIResponse(
                success=False,
                error=str(e)
            )
    
    def is_connected(self) -> bool:
        """Check if connected to API."""
        return self._connected and self.client is not None
    
    def disconnect(self):
        """Disconnect from API."""
        self.client = None
        self.api_key = ""
        self._connected = False
