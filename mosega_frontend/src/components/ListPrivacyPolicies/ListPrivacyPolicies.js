import React, {Component} from 'react';
import PrivacyPolicy from './PrivacyPolicy/PrivacyPolicy';
import { Grid, Segment } from 'semantic-ui-react';
import Aux from '../../hoc/Aux';
import axios from 'axios';

class ListPrivacyPolicies extends Component {

    state = {
        policies:[]
    }

    policyList = "";

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/PrivacyPolicyAPI/api/v1/PrivacyPolicy/')
            .then( response => {
                this.setState({policies:response.data});
                console.log(response);

                let policies = [...this.state.policies]

                this.policyList = policies.map(
                    policy =>(
                        <Grid.Row key={policy.id}>
                            <Grid.Column>
                                <Segment>
                                    <PrivacyPolicy policy ={policy.PrivacyPolicy} key={"PrivacyPolict_"+policy.id}/>
                                </Segment>
                            </Grid.Column>
                        </Grid.Row>
                    )
                );
            }

        );
    }



    render() {

        return (
            <Aux>
                <Grid padded>
                {
                    this.policyList
                }
                </Grid>
            </Aux>
        );


    }
}

export default ListPrivacyPolicies;


