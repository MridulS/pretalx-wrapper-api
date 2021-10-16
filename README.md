# pretalx-wrapper-api

Minimal wrapper around pretalx REST API.

Example usage:
``` python
In [1]: from pretalxapi import PreTalx

In [2]: url = "https://pretalx.com"

In [3]: api = PreTalx(url)

In [4]: api.get_events('pycon-2022').json()
Out[4]:
{'name': {'en': 'PyCon US 2022', 'es': 'PyCon US 2022'},
 'slug': 'pycon-2022',
 'is_public': True,
 'date_from': '2022-04-27',
 'date_to': '2022-05-01',
 'timezone': 'UTC',
 'urls': {'base': 'https://pretalx.com/pycon-2022/',
  'schedule': 'https://pretalx.com/pycon-2022/schedule/',
  'login': 'https://pretalx.com/pycon-2022/login/',
  'feed': 'https://pretalx.com/pycon-2022/schedule/feed.xml'}}
 
In [5]: api = PreTalx(url, token) # get your token from your user settings on pretalx.com

In [6]: api.validate_token()
Out[6]: <Response [200]>

In [7]: api.validate_token().json()
Out[7]:
{'email': 'test@example.com',
 'name': 'Example Singh',
 'locale': 'en',
 'timezone': 'Europe/Rome'}
```
