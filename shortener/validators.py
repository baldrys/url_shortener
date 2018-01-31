import requests
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from requests import exceptions

# from shortener.models import ShortURL
import shortener.models
from url_shortener.settings import SHORTCODE_MAX, SHORTCODE_MIN


def validate_url(url):
    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://' + url
    # print(url)
    url_validator = URLValidator()

    try:
        url_validator(url)
        r = requests.head(url)
        response_code = r.status_code
        # if 400 <= response_code < 600:  # x >=400 and x < 600
        if not (200<= response_code <400):
            # print('Status code = ', response_code)
            raise BadResponseCode
        # r = urllib.request.urlopen(url)

    # except (exceptions.InvalidURL, exceptions.MissingSchema, exceptions.InvalidSchema):
    #     raise ValidationError("Invalud URL")
    # except (HTTPError, URLError) as e:
    #     response_code = e.code
    #     if 400 <= response_code < 600:  # x >=400 and x < 600
    #         print('Status code = ', response_code)
    #     raise ValidationError("Bad response code: {0}".format(response_code))
    except (exceptions.ConnectionError, exceptions.ConnectTimeout):
        raise ValidationError("Connection problems")
    except BadResponseCode:
        # print(response_code)
        raise ValidationError("Bad response code: {0}".format(response_code))
    except ValidationError:
        # print(e)
        raise ValidationError("Invalid URL")
    return url

def validate_desired_shortcode(shortcode):
    # Klass = shortener.models.ShortURL()
    if SHORTCODE_MIN > len(shortcode):
        raise ValidationError("At least {0} symbols!".format(SHORTCODE_MIN))
    if len(shortcode) > SHORTCODE_MAX:
        raise ValidationError("{0} symbols maximum!".format(SHORTCODE_MAX))
    desired_shortcode = shortener.models.ShortURL.objects.filter(shortcode=shortcode)
    if desired_shortcode.exists():
        raise ValidationError("Desired short url already exists, try another one!")

class BadResponseCode(Exception):
    pass


