import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import history from '../history';
import { FormGroup, FormControl, Button } from 'react-bootstrap';
import { API_BASE_URL } from '../config';

function ConductTransaction() {
    const [amount, setAmount] = useState(0);
    const [recipient, setRecipient] = useState('');
    const [knownAddresses, setKnownAddresses] = useState([]);

    useEffect(() => {
        fetch(`${API_BASE_URL}/known-addresses`)
        .then(response => response.json())
        .then(json => setKnownAddresses(json));
    }, []);

    const updateRecipient = event => {
        setRecipient(event.target.value);
    }
    const updateAmount = event => {
        setAmount(Number(event.target.value));
    }
    const submitTransaction = () => {
        fetch(`${API_BASE_URL}/wallet/transact`,
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify({ recipient, amount })
        }).then(response => response.json())
          .then(json => {
              console.log('submitTransaction json', json);

              alert('Transaction Successful!!');

              history.push('/transaction-pool');

          })
    }

    return (
        <div className='ConductTransaction'>
            <Link to='/'>Home</Link>
            <hr />
            <h3>Conduct Transaction</h3>
            <br />
            <FormGroup className='ConductTransactionForm'>
                <FormControl
                    input='text' 
                    placeholder='recipient' 
                    value={recipient}
                    onChange={updateRecipient} 
                />
            </FormGroup >
            <br />
            <FormGroup className='ConductTransactionForm'>
            <FormControl
                    input='number' 
                    placeholder='amount' 
                    value={amount}
                    onChange={updateAmount} 
                />
            </FormGroup>
            <div>
                <Button
                    variant='info'
                    onClick={submitTransaction}
                >
                    Submit
                </Button>
            </div>
            <br />
            <h4>Known Addresses</h4>
            <div>
                {
                    knownAddresses.map((knownAddresses, i) => (
                        <span key={knownAddresses}>
                            <u>{knownAddresses}</u>
                            {i !== knownAddresses.length -1 ? ', ' : ''}
                        </span>
                    ))
                }
            </div>
        </div>
    )
}

export default ConductTransaction;