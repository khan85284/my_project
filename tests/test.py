"""
Unit tests for the scraper module.
"""

import pytest
from my_project85.scrapping import fetch_url
import aiohttp
from aioresponses import aioresponses


@pytest.mark.asyncio
async def test_fetch_url():
    """
    Test the fetch_url function with a mock response.
    """
    url = 'https://httpbin.org/get'
    html_content = "<html><head></head><body><h1>Example Domain</h1></body></html>"

    async with aiohttp.ClientSession() as session:
        with aioresponses() as m:
            m.get(url, status=200, body=html_content)
            fetched_url, content = await fetch_url(session, url)
            assert fetched_url == url
            assert content == html_content
