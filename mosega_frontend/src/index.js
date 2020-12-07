import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import axios from 'axios';
import policyReducer from './store/reducers/policyReducer';
import selectedPolicyReducer from './store/reducers/selectedPolicyReducer';
import termReducer from './store/reducers/termReducer';
import selectedTermReducer from './store/reducers/selectedTermReducer';
import similarityCheckReducer from './store/reducers/similarityCheckReducer';
import preClusterReducer from './store/reducers/preClusterReducer';
import similaritySetReducer from './store/reducers/similaritySetReducer';
import {createStore, combineReducers} from 'redux';
import {Provider} from 'react-redux';

const rootReducer = combineReducers({
    policies : policyReducer,
    selectedPolicy : selectedPolicyReducer,
    terms: termReducer,
    selectedTerm: selectedTermReducer,
    similarityCheck: similarityCheckReducer,
    preCluster: preClusterReducer,
    similaritySet: similaritySetReducer
});

const store = createStore(rootReducer);

axios.interceptors.request.use(request => {
        console.log(request);
        console.log('url : '+request.url);
        console.log('base url : '+request.baseURL);
        return request;
    }, error => {
        console.log(error);
        return Promise.reject(error);
    }
);

axios.interceptors.response.use(response => {
        console.log(response);
        return response;
    }, error => {
        console.log(error);
        return Promise.reject(error);
    }
);

ReactDOM.render(<Provider store={store}> <App /> </Provider>, document.getElementById('root'));

serviceWorker.unregister();
