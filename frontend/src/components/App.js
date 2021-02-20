import React, {useState, useEffect } from 'react'
import logo from '../assets/logo.png'

function App() {

  const [walletInfo, setWalletInfo] = useState({});

  useEffect(() => {
    fetch('http://localhost:5000/wallet/info')
    .then(response => response.json())
    .then(json => setWalletInfo(json));
  }, []);

  const {address, balance} = walletInfo;
  
  return (
    <div className="App">
      <img className="logo" src={logo} alt="application-logo"/>
      <h3>Python & React Blockchain App</h3> 
      <br />
      <div className="WalletInfo">
        <div>Address: {address}</div>
        <div>Balance: {balance}</div>
      </div>
    </div>
  );
}

export default App;
