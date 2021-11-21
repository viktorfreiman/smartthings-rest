import requests
from pprint import pprint


class SmartThingsError(Exception):
    pass


class SmartThings:
    def __init__(self, personal_access_token):
        # include api_key in all requested url the session
        self.apiendpoint = "https://api.smartthings.com/v1/"

        self._s = requests.Session()
        self._s.headers = {"Authorization": f"Bearer {personal_access_token}"}

    def _get(self, path):
        """
        Makes GET request, (auth is baked in to the session)
        Returns response as object
        """
        r = self._s.get(f"{self.apiendpoint}/{path}")

        if r.ok:
            return r.json()
        else:
            if r.status_code == 401:
                raise SmartThingsError("Unauthorized")

            # We got a bad error, raise it and wrapp the error msg for sending it up
            # this way we get a good error msg on every bad request
            try:
                r.raise_for_status()
            except requests.exceptions.HTTPError as error_msg:
                raise SmartThingsError(error_msg) from error_msg

    def capabilities(self):
        r = self._get("capabilities")
        return r["items"]

    def cap(self, cap_name, version=1):
        r = self._get(f"capabilities/{cap_name}/{version}")
        out = {
            "commands": [
                {
                    "component": "main",
                    "capability": cap_name,
                    "command": "setInputSource",
                    "arguments": ["HDMI1"],
                }
            ]
        }
        return out

    # def make_command():

    def devices(self):
        """Returns devices"""
        r = self._get("devices")
        return r["items"]

    def device(self, **kwargs):
        """Return first device to match key=value

        To get device with label "STV"
        >>> device(label="STV")
        """
        devices = self._get("devices")
        for device in devices["items"]:
            for match in kwargs:
                if device[match] == kwargs[match]:
                    return Device(device)
                    # return device


# class raw_st():
#     def __init__(self, personal_access_token):
#         self.url = "https://api.smartthings.com/v1/"
#         self._s = requests.Session()
#         self._s.headers = {"Authorization": f"Bearer {personal_access_token}"}

# class Device:
#     def __init__(self, data) -> None:
#         pass


class Device:
    def _version(self, version):
        return version

    def capability(self, num):
        """Hello from this capability"""
        pprint(f"{self.__dict__}")
        print(1 + num)

    def __init__(self, data) -> None:
        self.label = data["label"]
        self.component = data["components"][0]["id"]
        for capability in data["components"][0]["capabilities"]:
            # setattr(self, )o
            # print(capability)
            setattr(
                self,
                capability["id"],
                Capability(name=capability["id"], version=capability["version"]),
            )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.label})"


class Capability:
    def __init__(self, name, version) -> None:
        """Hello init"""
        self.name = name
        self.version = version

    def __call__(self, *args, **kwds):
        """Hello call"""
        print("you called me")
        print(f"I am {self.name}")

    def call(self, num):
        print(f"{self.name=}")
        return 1 + num
