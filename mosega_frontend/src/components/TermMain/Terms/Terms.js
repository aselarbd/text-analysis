import React, {Component} from 'react';
import { Card } from 'semantic-ui-react';
import Term from './Term/Term';
import * as actionType from '../../../store/action';
import {connect} from 'react-redux';
import classes from './Terms.css'

class Terms extends Component{

    goToURLHandler = (url) => {
        window.location.replace(url);
    };


    render() {

        const terms = this.props.terms.map(
            term => {
                return (
                    <Term
                        key={'term_'+term.id}
                        title={term.title}
                        goToURL={() => this.goToURLHandler(term.url)}
                        viewTerm={() => this.props.selectTermHandler(term.id)}
                    />
                );
            }
        );

        return(
            <div className={classes.Terms}>
                <Card.Group>
                    {terms}
                </Card.Group>
            </div>
        );
    }

}

const mapDispatchToProps = dispath => {
    return{
        selectTermHandler: (ID) => dispath({type:actionType.SELECT_TERM, selectedTermID:ID})
    }
};

export default connect(null,mapDispatchToProps) (Terms);