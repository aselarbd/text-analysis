import React, {Component} from 'react';
import { Card } from 'semantic-ui-react';
import Policy from './Policy/Policy';
import * as actionType from '../../store/action';
import {connect} from 'react-redux';
import classes from './Policies.css'

class Policies extends Component{

    goToURLHandler = (url) => {
        window.location.replace(url);
    };


    render() {

        const policies = this.props.policies.map(
            policy => {
                return (
                    <Policy
                        key={'policy_'+policy.id}
                        title={policy.title}
                        goToURL={() => this.goToURLHandler(policy.url)}
                        viewPolicy={() => this.props.selectPolicyHandler(policy.id)}
                    />
                );
            }
        );

        return(
            <div className={classes.Policies}>
                <Card.Group>
                    {policies}
                </Card.Group>
            </div>
        );
    }

}

const mapDispatchToProps = dispath => {
    return{
        selectPolicyHandler: (ID) => dispath({type:actionType.SELECT_POLICY, selectedPolicyID:ID})
    }
};

export default connect(null,mapDispatchToProps) (Policies);