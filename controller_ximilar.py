import os
import base64
from typing import Any, Dict, Optional
from threading import Lock

from dotenv import load_dotenv
from ximilar.client import RemoveBGClient, DominantColorGenericClient, GenericTaggingClient

load_dotenv()


class XimilarController:
    """Manages Ximilar API interactions using official Python SDK (Free Plan Services Only)."""

    def __init__(self, api_token: Optional[str] = None):
        self._api_token = api_token or os.getenv("XIMILAR_API_TOKEN")
        if not self._api_token:
            raise RuntimeError("XIMILAR_API_TOKEN not configured. Check your .env file.")
        self._lock = Lock()
        
        # Initialize only free plan services
        self._removebg_client = RemoveBGClient(token=self._api_token)
        self._color_client = DominantColorGenericClient(token=self._api_token)
        self._tagging_client = GenericTaggingClient(token=self._api_token)

    def remove_background(
        self,
        image_data: str,
        is_url: bool = True,
        model: str = "precise",
        binary_mask: bool = False,
        white_background: bool = False,
        image_format: str = "png",
        image_quality: int = 85
    ) -> Dict[str, Any]:
        """
        Remove background from image using SDK.
        
        Args:
            image_data: URL or base64 encoded image
            is_url: True if image_data is URL, False if base64
            model: "precise" or "fast"
            binary_mask: Include binary mask in response
            white_background: Include white background version in response
            image_format: Output format (png, jpg, webp)
            image_quality: JPEG/PNG quality (1-100)
        
        Returns:
            Dictionary with URLs to processed images
        """
        try:
            record = {"_url" if is_url else "_base64": image_data}
            
            if model == "precise":
                result = self._removebg_client.removebg_precise([record], image_format=image_format)
            else:
                result = self._removebg_client.removebg_fast([record], image_format=image_format)
            
            return result
        except Exception as e:
            return {"error": str(e), "status": {"code": 500, "text": "Request failed"}}

    def get_dominant_colors(
        self,
        image_data: str,
        is_url: bool = True,
        max_colors: int = 5
    ) -> Dict[str, Any]:
        """
        Extract dominant colors from image using SDK.
        
        Args:
            image_data: URL or base64 encoded image
            is_url: True if image_data is URL, False if base64
            max_colors: Maximum number of colors to extract
        
        Returns:
            Dictionary with dominant colors
        """
        try:
            record = {"_url" if is_url else "_base64": image_data}
            result = self._color_client.dominantcolor([record])
            return result
        except Exception as e:
            return {"error": str(e), "status": {"code": 500, "text": "Request failed"}}

    def tag_photo(
        self,
        image_data: str,
        is_url: bool = True
    ) -> Dict[str, Any]:
        """
        Tag a photo with descriptive labels using SDK.
        
        Args:
            image_data: URL or base64 encoded image
            is_url: True if image_data is URL, False if base64
        
        Returns:
            Dictionary with photo tags
        """
        try:
            record = {"_url" if is_url else "_base64": image_data}
            result = self._tagging_client.tags([record])
            return result
        except Exception as e:
            return {"error": str(e), "status": {"code": 500, "text": "Request failed"}}

    @staticmethod
    def image_to_base64(image_path: str) -> str:
        """Convert local image file to base64 string."""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def shutdown(self) -> None:
        """Close clients."""
        self._removebg_client = None
        self._color_client = None
        self._tagging_client = None


ximilar_controller = XimilarController()
