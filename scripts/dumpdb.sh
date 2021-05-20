#!/bin/bash

./manage.py dumpdata --exclude auth.permission --exclude contenttypes | json_pp > db.json

# to pretty-print the output, pipe it thru json_pp before redirecting it to db.json
