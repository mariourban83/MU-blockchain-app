## Python - React - Blockchain Application


**Activate virtual environment**
```
source venv/bin/activate
```

**Install required packages with :**
```
pip3 install -r requirements.txt
```

**Run the test in the venv**
```
python3 -m pytest backend/tests
```

**Run Flask server, with venv activated**
```
python3 -m backend.app
```

**Run Flask Peer Instance**
```
export PEER=True && python3 -m backend.app
```