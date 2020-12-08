import React, {Component} from 'react';
import {Card} from 'semantic-ui-react';
import Policy from '../../Shared/CardItem/CardItem';
import * as actionType from '../../../store/action';
import {connect} from 'react-redux';
import classes from './Policies.css';
import * as UTILS from '../../Shared/Utils/Utils';


class Policies extends Component{

    goToURLHandler = (url) => {
        window.location.replace(url);
    };

    deleteHandler = (policy_id) => {
        UTILS.deleteItems("policy",policy_id);
    };


    render() {

        const policies = this.props.policies.map(
            policy => {
                return (
                    <Policy
                        key={'policy_'+policy.id}
                        title={policy.title}
                        dataType= 'Privacy Policy'
                        goToURL={() => this.goToURLHandler(policy.url)}
                        viewItem={() => this.props.select_policy_handler(policy.id)}
                        deleteItem={() => this.deleteHandler(policy.id)}
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

const mapDispatchToProps = dispatch => {
    return{
        select_policy_handler: (ID) => dispatch({type:actionType.SELECT_POLICY, selectedPolicyID:ID})
    }
};

export default connect(null,mapDispatchToProps) (Policies);