import base64
script = b"""aW1wb3J0IG9zCmltcG9ydCBzeXMKCmRlZiBmYWNlYm9vaygpOgogICAgcGVydTEgPSAnIGRiL3Bl
cnUxLnR4dCcKICAgIHBlcnUyID0gJyBkYi9wZXJ1Mi50eHQnCiAgICBwcmludCgiIikKICAgIHVz
ZXIgPSBpbnB1dCgiSU5HUkVTRSBQQUxBQlJBIENMQVZFOiAiKQogICAgb3Muc3lzdGVtKCJncmVw
ICIgK3VzZXIgK3BlcnUxKQogICAgb3Muc3lzdGVtKCJncmVwICIgK3VzZXIgK3BlcnUyKQogICAg
cHJpbnQoIiIpCg=="""
exec(base64.b64decode(script))