import React, {Component} from 'react';
import PrivacyPolicy from './PrivacyPolicy/PrivacyPolicy';
import Aux from '../../hoc/Aux';
import axios from 'axios';

class ListPrivacyPolicies extends Component {

    backend_URL = 'http://www.mocky.io/v2/5d8d9ce4310000b6032b4f15'
    // backend_URL = 'http://127.0.0.1:8000/PrivacyPolicyAPI/api/v1/PrivacyPolicy/'

    state = {
        policies:[]
    }

    policyList = "";

    componentDidMount() {
        axios.get(this.backend_URL)
            .then( response => {
                this.setState({policies:response.data});
                console.log(response);

                let policies = [...this.state.policies];

                this.policyList = policies.map(
                    policy =>(
                            <PrivacyPolicy
                                policy ={policy.PrivacyPolicy}
                                key={"PrivacyPolict_"+policy.id}
                                policyURL={policy.policyurl}
                                policyTopic = {policy.topic}
                            />
                    )
                );
            }

        );
    }



    render() {

        return (
            <Aux> { this.policyList } </Aux>
        );


    }
}

export default ListPrivacyPolicies;


