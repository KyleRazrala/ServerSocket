#!/usr/bin/env python
import base64

encoded_code = """aW1wb3J0IHRpbWUKaW1wb3J0IG9zCnByaW50KCdreWxlJykKcHJpbnQoJ2FnZScpCmlucHV0KCc+Pj4gJykKcHJpbnQoJ3dhaXQnKQp0aW1lLnNsZWVwKDUpCg=="""

decoded_code = base64.b64decode(encoded_code).decode()

new_file = "decoded_script.py"

with open(new_file, "w") as file:
    file.write(decoded_code)

print("Nabalik sa normal na programa ang bagong file:", new_file)
