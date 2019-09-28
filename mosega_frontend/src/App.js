import React, {Component} from 'react';
import Layout from './components/Layout/Layout'
import AddPrivacyPolicy from './components/AddPrivacyPolicy/AddPrivacyPolicy'
import {BrowserRouter, Route} from "react-router-dom";
import ListPrivacyPolicies from './components/ListPrivacyPolicies/ListPrivacyPolicies'
import ListTerms from './components/ListTerms/ListTerms'
import AddTerms from './components/AddTerms/AddTerms'

class App extends Component {
  render() {
    return (
        <BrowserRouter>
            <div >
              <Layout>

                  <Route path="/add+policy" exact component={AddPrivacyPolicy}/>

                  <Route path="/list+policy" exact component={ListPrivacyPolicies}/>

                  <Route path="/add+terms" exact component={AddTerms}/>

                  <Route path="/list+terms" exact component={ListTerms}/>

              </Layout>
            </div>
        </BrowserRouter>
    );
  }

}

export default App;
