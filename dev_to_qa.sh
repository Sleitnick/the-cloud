#!/bin/bash

value="$(<auth.txt)"
python3 fetch_place.py dev.rbxl 7795117711 "$value"
