import os
from pprint import pprint
from smartthings_rest import SmartThings

# ks -> kickstart, demo file to experiment in

personal_access_token = os.environ.get("PAT")

st = SmartThings(personal_access_token)

# print(st.devices())
stv = st.device(label="STV")
