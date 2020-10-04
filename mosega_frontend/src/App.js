import React, {Component} from 'react';
import Layout from './components/Layout/Layout'
import {BrowserRouter, Route, Switch, Redirect} from "react-router-dom";

import PrivacyPolicy from './containers/PrivacyPolicy/PrivacyPolicy';
import TermAndCondition from './containers/TermAndCondition/TermAndCondition';
import Process from './containers/Process/Process';
import PreCluster from "./components/ProcessMain/PreCluster/PreCluster";
import SimilaritySet from "./components/ProcessMain/SimilaritySet/SimilaritySet";


class App extends Component {
  render() {
    return (
        <BrowserRouter>
            <div >
              <Layout>
                  <Switch>
                      <Route path="/policy" exact component={PrivacyPolicy}/>
                      <Route path="/term" exact component={TermAndCondition}/>
                      <Route path="/process" exact component={Process}/>
                      <Route path="/pre-cluster" exact component={PreCluster}/>
                      <Route path="/similarity-set" exact component={SimilaritySet}/>
                      <Redirect from='/' to='/policy' />
                  </Switch>


              </Layout>
            </div>
        </BrowserRouter>
    );
  }

}

export default App;
