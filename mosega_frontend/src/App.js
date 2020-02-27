import React, {Component} from 'react';
import Layout from './components/Layout/Layout'
import {BrowserRouter, Route, Switch, Redirect} from "react-router-dom";

import PrivacyPolicy from './containers/PrivacyPolicy/PrivacyPolicy';


class App extends Component {
  render() {
    return (
        <BrowserRouter>
            <div >
              <Layout>
                  <Switch>
                      <Route path="/policy" exact component={PrivacyPolicy}/>
                      <Redirect from='/' to='/policy' />
                  </Switch>


              </Layout>
            </div>
        </BrowserRouter>
    );
  }

}

export default App;
