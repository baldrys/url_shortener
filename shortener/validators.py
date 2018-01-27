from django.core.exceptions import ValidationError
from requests import exceptions
import requests
from django.core.validators import URLValidator

def validate_url(url):
    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://' + url
    try:
        r = requests.head(url)
        response_code = r.status_code
        if 400 <= response_code < 600:  # x >=400 and x < 600
            print('Status code = ', response_code)
            raise BadResponseCode
    # except (exceptions.InvalidURL, exceptions.MissingSchema, exceptions.InvalidSchema):
    #     raise ValidationError("Invalud URL")
    # except (exceptions.ConnectionError, exceptions.ConnectTimeout):
    #     raise ValidationError("Connection problems")
    except BadResponseCode:
        # print(response_code)
        raise ValidationError("Bad response code: {0}".format(response_code))
    except Exception as e:
        # print(e)
        raise ValidationError("Invalid URL")
    return url


class BadResponseCode(Exception):
    pass

