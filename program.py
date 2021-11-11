import os
from pprint import pprint

from smartthings_rest import SmartThings


def main():
    """
    personal_access_token (PAT) setup is the same as home-assistant

    https://www.home-assistant.io/integrations/smartthings/#personal-access-token-pat
    """
    # set PAT with export PAT="your_token"
    personal_access_token = os.environ.get("PAT", "")
    print(f"{personal_access_token=}")

    st = SmartThings(personal_access_token)
    pprint(st.devices())


if __name__ == "__main__":
    main()
