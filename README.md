# twitter follower's follower count

## setup

make credential file: `credential.py`.
and following set key and tokens:

```
API_KEY = ""
SECRET_KEY = ""
BEARAR_TOKEN = ""
ACCESS_TOKEN= ""
ACCESS_TOKEN_SECRET = ""
```

```console
% python3 -m venv venv
% . venv/bin/activate
% make pip
```

## execute

```console
% python get_follower.py
input username: susumuis  # input twitter username
```

and read `[username].output.csv`
