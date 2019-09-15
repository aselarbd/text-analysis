import React, {Component} from 'react';
import Layout from './components/Layout/Layout'
import AddPrivacyPolicy from './components/AddPrivacyPolicy/AddPrivacyPolicy'
import {BrowserRouter, Route} from "react-router-dom";
import ListPrivacyPolicies from './components/ListPrivacyPolicies/ListPrivacyPolicies'

class App extends Component {
  render() {
    return (
        <BrowserRouter>
            <div >
              <Layout>

                  <Route path="/add+policy" exact component={AddPrivacyPolicy}/>


                  <Route path="/list+policy" exact component={ListPrivacyPolicies}/>


              </Layout>
            </div>
        </BrowserRouter>
    );
  }

}

export default App;
