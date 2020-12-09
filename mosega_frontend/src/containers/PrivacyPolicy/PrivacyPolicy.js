import React, {Component} from 'react';
import axios from 'axios';
import * as URL from '../../constants/URL';

import NewPolicy from '../../components/PolicyMain/NewPolicy/NewPolicy';
import PolicyList from '../../components/PolicyMain/Policies/Policies';
import FullPolicy from '../../components/PolicyMain/FullPolicy/FullPolicy';
import SearchBar from '../../components/Shared/SearchBar/SearchBar';
import classes from './PrivacyPolicy.css';
import Aux from '../../hoc/Aux';


import {connect} from 'react-redux';
import * as actionType from '../../store/action';
import {Dimmer, Divider, Loader, Pagination, Segment} from "semantic-ui-react";

class PrivacyPolicy extends Component{

    state = {
      policies: null,
      totalPolicies: 0,
      searchList:null
    };

    componentDidMount() {
        axios.get(URL.GET_ALL_POLICIES)
            .then(resp => {
                this.setState({totalPolicies:resp.data.length});
                this.props.addPoliciesHandler(resp.data.reverse());
                this.setState({searchList:resp.data});
              this.setPoliciesForPage(0);
            });
    }

    setPoliciesForPage = (pageNo) => {
        const start = pageNo * 5;
        const end = start +5;
        this.setState({policies: this.props.policies.slice(start, end)});
    };


    pageChangeHandler = (event, pageInfo) => {
        this.setPoliciesForPage(pageInfo.activePage - 1);
    };

    render() {

        let searchList = null;
        if (this.state.searchList){
            searchList = <SearchBar
                items={this.state.searchList}
                button_text='View Policy'
                data_type='Privacy Policy'
                type='policy'
            />;
        }

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
                    {searchList}
                    <br/>
                    <Divider
                        horizontal
                        style={{marginLeft:"10px", marginRight:"10px", marginTop:"20px"}}
                    >
                        Policy List
                    </Divider>
                    <br/><br/>
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
                    <br/>
                    <Divider
                        horizontal
                        style={{marginLeft:"10px", marginRight:"10px", marginTop:"20px"}}
                    >
                        Add New Policy
                    </Divider>
                    <br/><br/>
                    <NewPolicy />
                </div>
                <div>
                    <br/>
                    <Divider
                        horizontal
                        style={{marginLeft:"10px", marginRight:"10px", marginTop:"20px"}}
                    >
                        View Full Policy
                    </Divider>
                    <br/><br/>
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

const mapDispatchToProps = dispatch => {
    return{
        addPoliciesHandler: (policies) => dispatch({type:actionType.LOAD_POLICIES, payload: policies})
    }
};

export default connect(mapStateToProps,mapDispatchToProps) (PrivacyPolicy);