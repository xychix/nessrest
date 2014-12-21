import imp
ness6rest = imp.load_source('ness6rest', '../ness6rest.py')

ness6rest.requests.packages.urllib3.disable_warnings()

import requests_mock


class TestScanner:
  def test_init(self):
    url = "https://localhost:8834"
    login = "login"
    password = "password"
    with requests_mock.Mocker() as mock:
      mock.register_uri('POST', url + '/session', text='{"token":"mock_token"}')
      mock.register_uri('GET', url + '/session', text=
      """{
        "permissions":"128"
      }""")
      mock.register_uri('GET', url + '/server/properties', text=
      """{
        "nessus_ui_version":"6.1.1",
        "server_version":"6.1.0",
        "feed":"ProFeed",
        "loaded_plugin_set":"lol"
      }""")
      # TODO: make these mocks 'global' so that they are used at the exit of the program
      # when the delete method is called
      mock.register_uri('DELETE', 'https://localhost:8834/session', text='{}')
      scan = ness6rest.Scanner(url=url, login=login, password=password)
      assert scan
