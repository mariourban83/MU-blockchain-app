[![Build Status](https://travis-ci.com/mariourban83/MU-blockchain-app.svg?branch=main)](https://travis-ci.com/mariourban83/MU-blockchain-app)

* * * 

## Python - React - Blockchain Application   
#### Local Deployment   
Python => 3.7 required 

**Create virtual env in root directory with**
```
python3 -m venv venv
```

**Activate virtual environment**
```
source venv/bin/activate
```

**From the app root directory, install python required packages with :**
```
pip3 install -r requirements.txt
```

**Run the test in the venv**
```
python3 -m pytest backend/tests
```

**Seed data at the startup and start Flask server with the env activated:**
```
export SEED_DATA=True && python3 -m backend.app
```

**Run Flask Peer Instance**
```
export PEER=True && python3 -m backend.app
```

**Install dependencies for react and run the frontend application**
cd into /frontend directory:
```
npm install
npm run start
```
