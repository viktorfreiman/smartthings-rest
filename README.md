# Smartthings-rest

NOTE! work in progress

Smart and straightforward lib for controlling things with <https://www.smartthings.com/>  

- [Smartthings-rest](#smartthings-rest)
- [simple json printout of all](#simple-json-printout-of-all)
- [draft how working code will look like](#draft-how-working-code-will-look-like)
- [returns status / bool](#returns-status--bool)
- [Turn device on](#turn-device-on)
- [Turn device off](#turn-device-off)

[Offical smartthings docs](https://developer-preview.smartthings.com/docs/getting-started/welcome)

~~~py
# simple json printout of all 
from smartthings_rest import SmartThings

st = SmartThings(personal_access_token)

print(st.devices())

~~~

~~~py
# draft how working code will look like
stv = st.device(label="STV")

# returns status / bool
stv.switch.on

stv.audioVolume.volumeDown
stv.audioVolume.setVolume = 10

stv.mediaInputSource.setInputSource = "HDM1"

~~~

~~~sh
export PAT="your_pat"
python3 hello_smartthings.py
~~~

~~~text
Urls to add

https://api.smartthings.com/v1/devices/deviceId/status

https://api.smartthings.com/v1/devices/deviceId/components/main/capabilities/mediaInputSource/status

---
# Turn device on
https://api.smartthings.com/v1/devices/deviceId/commands

{
    "commands": [
        {
            "component": "main",
            "capability": "switch",
            "command": "on"
        }
    ]
}

# Turn device off
https://api.smartthings.com/v1/devices/deviceId/commands

{
    "commands": [
        {
            "component": "main",
            "capability": "switch",
            "command": "off"
        }
    ]
}

https://api.smartthings.com/v1/capabilities

https://api.smartthings.com/v1/capabilities/switch/1

~~~
