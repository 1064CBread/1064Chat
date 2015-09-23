"""
Utilities specific to REST blueprints.
"""
from enum import Enum
import re


class ClientType(str, Enum):
    BROWSER = "browser"  # most useful in debug
    CURL = "cURL"  # also useful in debug
    OTHER = "other"  # usually production apps


browsers = re.compile("|".join(("chrome", "firefox", "safari", "opera")), re.IGNORECASE)


def get_implied_client_type(useragent: str) -> ClientType:
    """
    Attempts to get the client type based on user-agent. This is by no means exaustive for browser checking,
    and may be incorrect if the client lies.
    :param useragent: The user-agent that the client provided
    :return: The ClientType the user-agent implies
    """
    if browsers.search(useragent):
        return ClientType.BROWSER
    if "curl/" in useragent:
        return ClientType.CURL
    return ClientType.OTHER
