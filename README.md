[![Build Status](https://travis-ci.com/mariourban83/blockchainApplication1.svg?token=Vzs1sAouQtMgjq4uyHeY&branch=main)](https://travis-ci.com/mariourban83/blockchainApplication1)

* * * 

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

**Run the frontend React Application**
From the frontend directory:
```
npm run start
```

**Seed data at the startup**
with the env activated:
```
export SEED_DATA=True && python3 -m backend.app
```

