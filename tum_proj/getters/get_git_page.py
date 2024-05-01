import requests
from pydantic import validate_call
import ioc


@validate_call
def get_github_page(link: str) -> str:
    parser_type: str = ioc.require('GitHub.Request.Parser')
    header: dict = ioc.require('GitHub.Request.Header')
    req = requests.get(
        link, 
        parser_type, 
        headers=header,
    )
    return req.text