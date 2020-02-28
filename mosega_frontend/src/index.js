import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import axios from 'axios';
import * as URL from './constants/URL';
import policyReducer from './store/reducers/policyReducer';
import selectedPolicyReducer from './store/reducers/selectedPolicyReducer';
import termReducer from './store/reducers/termReducer';
import selectedTermReducer from './store/reducers/selectedTermReducer';
import {createStore, combineReducers} from 'redux';
import {Provider} from 'react-redux';

const rootReducer = combineReducers({
    policies : policyReducer,
    selectedPolicy : selectedPolicyReducer,
    terms: termReducer,
    selectedTerm: selectedTermReducer
});

const store = createStore(rootReducer);

axios.defaults.baseURL =URL.BASE_URL;

ReactDOM.render(<Provider store={store}> <App /> </Provider>, document.getElementById('root'));

serviceWorker.unregister();
