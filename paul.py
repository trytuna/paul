#!/usr/bin/env python3

import http.client
import urllib.parse
import sys
import argparse

__version__ = "1.0.0"
__prowlapi__ = "api.prowlapp.com"


class Paul(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "paul/%s" % str(__version__),
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/xml"
        }
        self.prowlapi = str(__prowlapi__)

    """
    apikey -> API keys separated by commas. Each API key is a 40-byte
              hexadecimal string
    application -> 256Bytes
    event -> 1024Bytes
    description -> 10000Bytes
    url -> 512Bytes
    priority -> -2 to 2. Default is 0
        -2 Very Low
        -1 Moderate
         0 Normal
         1 High
         2 Emergency
    providerkey -> 40Bytes

    """
    def push(self, apikey, application, event, description, url=None,
             priority=None, providerkey=None):
        data = dict()

        if(len(apikey) == 40 and type(apikey) is str):
            data["apikey"] = apikey
        elif(len(apikey) > 1 and type(apikey) is list):
            ",".join(apikey)
        else:
            print("Incorrect API Key!")
            sys.exit(1)

        data["application"] = application[:256]
        data["event"] = event[:1024]
        data["description"] = description[:10000]

        if url:
            data["url"] = url
        if priority:
            data["priority"] = priority
        if providerkey:
            data["providerkey"] = providerkey

        parameters = urllib.parse.urlencode(data)
        parameters = parameters.encode('utf-8')

        conn = http.client.HTTPConnection(__prowlapi__, 80)
        conn.request("POST", "/publicapi/add", parameters, self.headers)
        response = conn.getresponse()

        # XML output
        output = response.read()

        conn.close()

        if(response.status == 200):
            return True
        elif(response.status == 400):
            raise Exception("Bad request, the parameters you provided did not "
                            "validate")
        elif(response.status == 401):
            raise Exception("Not authorized, the API key (%s) given is not "
                            "valid, and does not correspond to a user", apikey)
        elif(response.status == 406):
            raise Exception("Not acceptable, your IP address has exceeded the "
                            "API limit")
        elif(response.status == 409):
            raise Exception("Not approved, the user has yet to approve your "
                            "retrieve request")
        elif(response.status == 500):
            raise Exception("Internal server error, something failed to "
                            "execute properly on the Prowl side")
