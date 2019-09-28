import React, {Component} from 'react';
import Term from './Term/Term';
import Aux from '../../hoc/Aux';
import axios from 'axios';

class ListTerms extends Component {

    backend_URL = 'http://www.mocky.io/v2/5d8f2f803200005d00adeba2';
    // backend_URL = 'http://127.0.0.1:8000/PrivacyPolicyAPI/api/v1/PrivacyPolicy/'

    state = {
        terms:[]
    }

    termList = "";

    componentDidMount() {
        axios.get(this.backend_URL)
            .then( response => {
                    this.setState({terms:response.data});
                    console.log(response);

                    let terms = [...this.state.terms];

                    this.termList = terms.map(
                        term =>(
                            <Term
                                term ={term.term}
                                key={"term_"+term.id}
                                termURL={term.termURLl}
                                termTopic = {term.topic}
                            />
                        )
                    );
                }

            );
    }



    render() {

        return (
            <Aux> { this.termList } </Aux>
        );


    }
}

export default ListTerms;


