"""Test custom_fields."""

from unittest.mock import patch

from pypaperless import Paperless
from pypaperless.api import CustomFieldEndpoint, EndpointCUDMixin, PaginatedResult
from pypaperless.models import CustomField
from pypaperless.models.shared import CustomFieldType


async def test_endpoint(paperless: Paperless) -> None:
    """Test endpoint."""
    assert isinstance(paperless.custom_fields, CustomFieldEndpoint)
    assert isinstance(paperless.custom_fields, EndpointCUDMixin)


async def test_list_and_get(paperless: Paperless, data):
    """Test list."""
    with patch.object(paperless, "request", return_value=data["custom_fields"]):
        result = await paperless.custom_fields.list()

        assert isinstance(result, list)
        assert len(result) > 0

        page = await paperless.custom_fields.get()

        assert isinstance(page, PaginatedResult)
        assert len(page.items) > 0
        assert isinstance(page.items.pop(), CustomField)


async def test_one(paperless: Paperless, data):
    """Test one."""
    with patch.object(paperless, "request", return_value=data["custom_fields"]["results"][0]):
        item = await paperless.custom_fields.one(72)

        assert isinstance(item, CustomField)
        assert isinstance(item.data_type, CustomFieldType)