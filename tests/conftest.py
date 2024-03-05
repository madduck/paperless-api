"""Setup pytest."""

from collections.abc import AsyncGenerator, Generator
from typing import Any

from aioresponses import aioresponses
import pytest

from pypaperless import Paperless
from pypaperless.const import API_PATH

from .const import PAPERLESS_TEST_REQ_ARGS, PAPERLESS_TEST_TOKEN, PAPERLESS_TEST_URL
from .data import PATCHWORK

# mypy: ignore-errors


@pytest.fixture(name="resp")
def aioresponses_fixture() -> Generator[aioresponses, None, None]:
    """Return aioresponses fixture."""
    with aioresponses() as m:
        yield m


@pytest.fixture(name="api_latest")
async def api_version_latest_fixture(api_23) -> AsyncGenerator[Paperless, Any]:
    """Return a Paperless object with latest version."""
    yield api_23


@pytest.fixture(name="api")
def api_obj_fixture() -> Paperless:
    """Return Paperless."""
    paperless = Paperless(
        PAPERLESS_TEST_URL,
        PAPERLESS_TEST_TOKEN,
        request_args=PAPERLESS_TEST_REQ_ARGS,
    )
    return paperless


@pytest.fixture(name="api_00")
async def api_version_00_fixture(resp: aioresponses, api) -> AsyncGenerator[Paperless, Any]:
    """Return a basic Paperless object."""
    resp.get(
        f"{PAPERLESS_TEST_URL}{API_PATH['index']}",
        status=200,
        headers={"X-Version": "0.0.0"},
        payload=PATCHWORK["paths_v0_0_0"],
    )
    async with api:
        yield api


@pytest.fixture(name="api_18")
async def api_version_18_fixture(resp: aioresponses, api) -> AsyncGenerator[Paperless, Any]:
    """Return a Paperless object with given version."""
    resp.get(
        f"{PAPERLESS_TEST_URL}{API_PATH['index']}",
        status=200,
        headers={"X-Version": "1.8.0"},
        payload=PATCHWORK["paths_v1_8_0"],
    )
    async with api:
        yield api


@pytest.fixture(name="api_117")
async def api_version_117_fixture(resp: aioresponses, api) -> AsyncGenerator[Paperless, Any]:
    """Return a Paperless object with given version."""
    resp.get(
        f"{PAPERLESS_TEST_URL}{API_PATH['index']}",
        status=200,
        headers={"X-Version": "1.17.0"},
        payload=PATCHWORK["paths_v1_17_0"],
    )
    async with api:
        yield api


@pytest.fixture(name="api_20")
async def api_version_20_fixture(resp: aioresponses, api) -> AsyncGenerator[Paperless, Any]:
    """Return a Paperless object with given version."""
    resp.get(
        f"{PAPERLESS_TEST_URL}{API_PATH['index']}",
        status=200,
        headers={"X-Version": "2.0.0"},
        payload=PATCHWORK["paths_v2_0_0"],
    )
    async with api:
        yield api


@pytest.fixture(name="api_23")
async def api_version_23_fixture(resp: aioresponses, api) -> AsyncGenerator[Paperless, Any]:
    """Return a Paperless object with given version."""
    resp.get(
        f"{PAPERLESS_TEST_URL}{API_PATH['index']}",
        status=200,
        headers={"X-Version": "2.3.0"},
        payload=PATCHWORK["paths_v2_3_0"],
    )
    async with api:
        yield api
