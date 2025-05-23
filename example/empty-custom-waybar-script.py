#!/usr/bin/env python

import json

return_dict = {
        "text": "test",
        "tooltip": "test\n   tooltip",
        "class": "test-class",
        "percentage": 90,
        }

return_json = json.dumps(return_dict)

print(return_json)
