import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { createBrowserHistory } from 'history';
import './index.css';
import App from './components/App';
import Blockchain from './components/Blockchain';
import ConductTransaction from './components/ConductTransaction';
import TransactionPool from './components/TransactionPool';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <Switch>
        <Route exact path="/" component={App} />
        <Route path='/blockchain' component={Blockchain} />
        <Route path='/Conduct-transaction' component={ConductTransaction} />
        <Route path='/transaction-pool' component={TransactionPool} />
      </Switch>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
