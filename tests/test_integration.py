"""
Integration tests for myair-py client
Copy .env.example to .env and update with your credentials.
"""
import aiohttp
import os
import pytest
from pathlib import Path
from dotenv import load_dotenv
from myair_py import ClientFactory, MyAirConfig, AuthenticationError

@pytest.fixture(scope="session")
def test_config():
    """Load test configuration from .env file"""
    # Load from project root
    env_path = Path(__file__).parent.parent / ".env"
    load_dotenv(env_path)
    
    username = os.getenv("MYAIR_USERNAME")
    password = os.getenv("MYAIR_PASSWORD")
    region = os.getenv("MYAIR_REGION", "NA")
    
    if not username or not password:
        pytest.skip("Please copy .env.example to .env and update with your credentials")
    
    return MyAirConfig(username=username, password=password, region=region)

@pytest.fixture
async def client_session():
    """Create aiohttp session with cookie jar"""
    jar = aiohttp.CookieJar(unsafe=True)
    async with aiohttp.ClientSession(cookie_jar=jar) as session:
        yield session

@pytest.fixture
async def myair_client(test_config, client_session):
    """Create authenticated MyAir client"""
    client = ClientFactory(test_config, client_session).get()
    await client.connect()
    return client

@pytest.mark.integration
@pytest.mark.asyncio
async def test_authentication(test_config, client_session):
    """Test authentication flow"""
    client = ClientFactory(test_config, client_session).get()
    await client.connect()  # Should not raise an exception

@pytest.mark.integration
@pytest.mark.asyncio
async def test_device_data(myair_client):
    """Test device data retrieval"""
    device_data = await myair_client.get_user_device_data()
    
    assert device_data is not None
    assert isinstance(device_data, dict)
    # Basic validation that we got device info
    assert "deviceType" in device_data or "serialNumber" in device_data

@pytest.mark.integration
@pytest.mark.asyncio  
async def test_sleep_records(myair_client):
    """Test sleep records retrieval"""
    sleep_records = await myair_client.get_sleep_records()
    
    assert sleep_records is not None
    assert isinstance(sleep_records, list)
    # Should return some records (could be empty for new users)
    assert len(sleep_records) >= 0

