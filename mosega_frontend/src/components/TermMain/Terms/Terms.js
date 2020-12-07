import React, {Component} from 'react';
import { Card } from 'semantic-ui-react';
import Term from '../../Shared/CardItem/CardItem';
import * as actionType from '../../../store/action';
import {connect} from 'react-redux';
import classes from './Terms.css';

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
                        buttonText='View Term'
                        dataType= 'Terms of Conditions'
                        goToURL={() => this.goToURLHandler(term.url)}
                        viewItem={() => this.props.selectTermHandler(term.id)}
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

const mapDispatchToProps = dispatch => {
    return{
        selectTermHandler: (ID) => dispatch({type:actionType.SELECT_TERM, selectedTermID:ID})
    }
};

export default connect(null,mapDispatchToProps) (Terms);