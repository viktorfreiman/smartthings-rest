a = {
    "id": "mediaInputSource",
    "version": 1,
    "status": "proposed",
    "name": "Media Input Source",
    "attributes": {
        "supportedInputSources": {
            "schema": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "array",
                        "items": {
                            "title": "MediaSource",
                            "type": "string",
                            "enum": [
                                "AM",
                                "CD",
                                "FM",
                                "HDMI",
                                "HDMI1",
                                "HDMI2",
                                "HDMI3",
                                "HDMI4",
                                "HDMI5",
                                "HDMI6",
                                "digitalTv",
                                "USB",
                                "YouTube",
                                "aux",
                                "bluetooth",
                                "digital",
                                "melon",
                                "wifi",
                            ],
                        },
                    }
                },
                "additionalProperties": False,
                "required": ["value"],
            },
            "enumCommands": [],
        },
        "inputSource": {
            "schema": {
                "type": "object",
                "properties": {
                    "value": {
                        "title": "MediaSource",
                        "type": "string",
                        "enum": [
                            "AM",
                            "CD",
                            "FM",
                            "HDMI",
                            "HDMI1",
                            "HDMI2",
                            "HDMI3",
                            "HDMI4",
                            "HDMI5",
                            "HDMI6",
                            "digitalTv",
                            "USB",
                            "YouTube",
                            "aux",
                            "bluetooth",
                            "digital",
                            "melon",
                            "wifi",
                        ],
                    }
                },
                "additionalProperties": False,
                "required": ["value"],
            },
            "setter": "setInputSource",
            "enumCommands": [],
        },
    },
    "commands": {
        "setInputSource": {
            "arguments": [
                {
                    "name": "mode",
                    "optional": False,
                    "schema": {
                        "title": "MediaSource",
                        "type": "string",
                        "enum": [
                            "AM",
                            "CD",
                            "FM",
                            "HDMI",
                            "HDMI1",
                            "HDMI2",
                            "HDMI3",
                            "HDMI4",
                            "HDMI5",
                            "HDMI6",
                            "digitalTv",
                            "USB",
                            "YouTube",
                            "aux",
                            "bluetooth",
                            "digital",
                            "melon",
                            "wifi",
                        ],
                    },
                }
            ]
        }
    },
}


class Capability:
    def _version(self, version):
        return version

    def __init__(self, data) -> None:
        # self.component = data["components"][0]["id"]
        # for capabilities in data["components"][0]["capabilities"][0]:
        #     setattr(self, )

        for key, value in data.items():
            setattr(self, key, value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"

