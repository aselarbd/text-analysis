import React, {Component} from 'react';
import axios from 'axios';
import * as URL from '../../constants/URL';

import NewTerm from '../../components/TermMain/NewTerm/NewTerm';
import TermList from '../../components/TermMain/Terms/Terms';
import FullTerm from '../../components/TermMain/FullTerm/FullTerm';
import classes from './TermAndCondition.css';
import Aux from '../../hoc/Aux';


import {connect} from 'react-redux';
import * as actionType from '../../store/action';
import {Dimmer, Loader, Pagination, Segment} from "semantic-ui-react";

class TermAndCondition extends Component{

    state = {
        terms: null,
        totalTerms: 0
    };
    componentDidMount() {
        axios.get(URL.GET_ALL_TERMs)
            .then(resp => {
                this.setState({totalTerms:resp.data.length});
                this.props.addTermsHandler(resp.data.reverse());
                this.setTermsForPage(0);
            });
    }

    setTermsForPage = (pageNo) => {
        const start = pageNo * 5;
        const end = start +5;
        this.setState({terms: this.props.terms.slice(start, end)});
    };


    pageChangeHandler = (event, pageInfo) => {
        this.setTermsForPage(pageInfo.activePage - 1);
    };

    render() {

        let terms = (
            <Segment style={{marginLeft: "10px", marginRight: "10px", height:"400px"}}>
                <Dimmer active inverted>
                    <Loader size='large'> Terms are Loading ...</Loader>
                </Dimmer>
            </Segment>
        );

        if (this.state.terms){
            terms = (
                <Aux>
                    <TermList terms={this.state.terms}/>
                    <div className={classes.TermPagination}>
                        <Pagination
                            onPageChange = {(event,data)=>this.pageChangeHandler(event,data)}
                            boundaryRange={0}
                            defaultActivePage={1}
                            ellipsisItem={null}
                            firstItem={null}
                            lastItem={null}
                            siblingRange={1}
                            totalPages={Math.ceil(this.state.totalTerms/5)}
                        />
                    </div>
                </Aux>
            );
        }

        return(
            <div>
                <div>
                    {terms}
                </div>
                <div>
                    <NewTerm />
                </div>
                <div>
                    <FullTerm />
                </div>
            </div>
        );
    }
}

const mapStateToProps = state => {
    return {
        terms: state.terms.terms
    }
};

const mapDispatchToProps = dispatch => {
    return{
        addTermsHandler: (terms) => dispatch({type:actionType.LOAD_TERMS, payload: terms})
    }
};

export default connect(mapStateToProps,mapDispatchToProps) (TermAndCondition);