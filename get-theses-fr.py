#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
import sys

__author__ = "François-Xavier Coudert"
__license__ = "MIT"

BASE_URL = "https://www.theses.fr/?q=*:*"


def main():
    r = requests.get(BASE_URL + "&start=0&format=json")
    r = r.json()

    n = r["response"]["numFound"]
    print(f"Found {n} results")

    data = r["response"]["docs"]
    i = 0

    while True:
        i += 1000
        r = requests.get(BASE_URL + f"&start={i}&format=json")
        r = r.json()
        docs = r["response"]["docs"]

        data.extend(docs)
        print(f"Documents downloaded: {len(data)}")
        if len(docs) < 1000:
            break

    print(f"Output {len(data)} records to file")
    with open("theses-fr.json", "w") as f:
        json.dump(data, f)
    print("Done")

    sys.exit(0)


if __name__ == '__main__':
    main()
