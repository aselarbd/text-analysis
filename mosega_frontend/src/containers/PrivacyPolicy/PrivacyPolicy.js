import React, {Component} from 'react';
import axios from 'axios';
import * as URL from '../../constants/URL';

import NewPolicy from '../../components/NewPolicy/NewPolicy';
import PolicyList from '../../components/Policies/Policies';
import FullPolicy from '../../components/FullPolicy/FullPolicy';
import classes from './PrivacyPolicy.css';
import Aux from '../../hoc/Aux';


import {connect} from 'react-redux';
import * as actionType from '../../store/action';
import {Dimmer, Loader, Pagination, Segment} from "semantic-ui-react";

class PrivacyPolicy extends Component{

    state = {
      policies: null,
      pageNumber: 0,
      totalPolicies: 0
    };

    componentDidMount() {
        const endPoint= URL.GET_ALL_POLICIES;
        const test = "http://www.mocky.io/v2/5e57e8ea3000003d00fd3ea5";
        axios.get(test)
            .then(resp => {
                console.log(resp.data);
                this.setState({totalPolicies:resp.data.length});
                this.props.addPoliciesHandler(resp.data);
              this.setPoliciesForPage(0);
            });
    }

    setPoliciesForPage = (pageNo) => {
        const start = pageNo * 5;
        const end = start +5;
        this.setState({policies: this.props.policies.slice(start, end)});
        console.log('start : '+ start+' end : '+end);
    };


    pageChangeHandler = (event, pageInfo) => {
        this.setPoliciesForPage(pageInfo.activePage - 1);
    };

    render() {

        let policies = (
            <Segment style={{marginLeft: "10px", marginRight: "10px", height:"400px"}}>
                <Dimmer active inverted>
                    <Loader size='large'> Policies are Loading ...</Loader>
                </Dimmer>
            </Segment>
        );

        if (this.state.policies){
            policies = (
                <Aux>
                    <PolicyList policies={this.state.policies}/>
                    <div className={classes.PolicyPagination}>
                        <Pagination
                            onPageChange = {(event,data)=>this.pageChangeHandler(event,data)}
                            boundaryRange={0}
                            defaultActivePage={1}
                            ellipsisItem={null}
                            firstItem={null}
                            lastItem={null}
                            siblingRange={1}
                            totalPages={Math.ceil(this.state.totalPolicies/5)}
                        />
                    </div>
                </Aux>
            );

        }

        return(
            <div>
                <div>
                    {policies}
                </div>
                <div>
                    <NewPolicy />
                </div>
                <div>
                    <FullPolicy />
                </div>
            </div>
        );
    }
}

const mapStateToProps = state => {
  return {
      policies: state.policies.policies
  }
};

const mapDispatchToProps = dispath => {
    return{
        addPoliciesHandler: (policies) => dispath({type:actionType.LOAD_POLICIES, payload: policies})
    }
};

export default connect(mapStateToProps,mapDispatchToProps) (PrivacyPolicy);