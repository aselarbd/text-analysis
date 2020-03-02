import React, {Component} from 'react';
import _ from 'lodash';
import {Search, Grid, Card, Message} from 'semantic-ui-react';
import classes from './SearchBar.css';
import Result from '../../Shared/CardItem/CardItem';
import Aux from './../../../hoc/Aux';
import * as actionType from "../../../store/action";
import {connect} from 'react-redux';

class SearchBar extends Component {

    source = this.props.items;

    state = {
        isLoading: false,
        results: [],
        value: ''
    };

    goToURLHandler = (url) => {
        window.location.replace(url);
    };

    handleResultSelect = (e, { result }) => {
        this.setState({ value: result.title });
    };

    handleSearchChange = (e, { value }) => {
        this.setState({ isLoading: true, value });

        setTimeout(() => {
            if (this.state.value.length < 1) return this.setState({ isLoading: false, results: [], value: '' });

            const re = new RegExp(_.escapeRegExp(this.state.value), 'i');
            const isMatch = (result) => re.test(result.title);

            this.setState({
                isLoading: false,
                results: _.filter(this.source, isMatch)
            });
        }, 300)
    };


    render() {

        const { isLoading, value, results } = this.state;

        let searchResult = <Message
            style={{textAlign:"center", marginLeft: "20px", marginRight: "20px", width:"98vw"}}
            floating
        >
            Search results ...
        </Message>;

        if (!this.state.isLoading && this.state.results.length > 0) {
            searchResult = this.state.results.map(item => (
                <Result
                    key={'search_'+item.id}
                    title={item.title}
                    buttonText= {this.props.buttonText}
                    dataType= {this.props.dataType}
                    goToURL={() => this.goToURLHandler(item.url)}
                    viewItem={() => {
                        if (this.props.type==='policy') {this.props.selectPolicyHandler(item.id);}
                        if (this.props.type==='term') {this.props.selectTermHandler(item.id);}
                        }
                    }
                />
            )
            );
        }

        return (
            <Aux>
                <div>
                    <Grid >
                        <Grid.Column  width={15}>
                            <div className={classes.SearchBar}>
                                <Search
                                    fluid
                                    size='huge'
                                    loading={isLoading}
                                    onResultSelect={this.handleResultSelect}
                                    onSearchChange={_.debounce(this.handleSearchChange, 500, {
                                        leading: true,
                                    })}
                                    results={results}
                                    value={value}
                                    minCharacters={2}
                                    {...this.props}
                                />
                            </div>
                        </Grid.Column>
                    </Grid>
                </div>
                <div className={classes.searchResult}>
                    <Card.Group>
                        {searchResult}
                    </Card.Group>
                </div>
            </Aux>
        );
    }
}

const mapDispatchToProps = dispatch => {
    return{
        selectPolicyHandler: (ID) => dispatch({type:actionType.SELECT_POLICY, selectedPolicyID:ID}),
        selectTermHandler: (ID) => dispatch({type:actionType.SELECT_TERM, selectedTermID:ID})
    }
};

export default connect(null,mapDispatchToProps) (SearchBar);