import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import axios from 'axios';
import * as URL from './constants/URL';


import {createStore, combineReducers} from 'redux';

axios.defaults.baseURL =URL.BASE_URL;


    ReactDOM.render(<App />, document.getElementById('root'));

serviceWorker.unregister();
