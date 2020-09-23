import React, {Component} from 'react';
import {Button, Card, Input} from 'semantic-ui-react';
import {withRouter} from 'react-router-dom';
import {connect} from 'react-redux';
import * as actionType from '../../../store/action';

class cardDeck extends Component{

    state={
        similarityTextBox:''
    };

    similarityTextBoxHandler = (event) => {
        this.setState({similarityTextBox:event.target.value});
    };

    similarityTextBoxButtonHandler = () => {
        if (this.state.similarityTextBox !== ''){
            this.props.addSimilarityQuery({query:this.state.similarityTextBox, queryType:this.props.displayType});

            this.props.history.push({
                pathname:"/process",
            });
        }
    };


    findClauses = () => {
        this.props.addSimilarityQuery({query:this.props.heading, queryType:this.props.displayType});

        this.props.history.push({
            pathname:"/process",
        });
    };

    render() {

        let controlPanel = null;

        if (this.props.displayType === "policy" || this.props.displayType === "term"){
            controlPanel = <div>
                <Button basic color='black' onClick={this.findClauses}>Find Similar clauses based on Topic </Button>
                <Input style={{marginLeft: "20px", marginRight: "20px"}}
                       size='large' icon='search'
                       placeholder='Search Similarity phrases ...'
                       value={this.state.similarityTextBox}
                       onChange={this.similarityTextBoxHandler}
                />
                <Button basic color='black'
                        size='large'
                        onClick={this.similarityTextBoxButtonHandler}
                >Search </Button>

            </div>
        }

        return (
            <Card fluid style ={{"margin":"10px", "width":"98%"}} >
                <Card.Content>
                    <Card.Header>{this.props.heading}</Card.Header>
                    <Card.Meta>{this.props.meta}</Card.Meta>
                    <Card.Description>{this.props.text}</Card.Description>
                </Card.Content>
                <Card.Content extra>
                    {controlPanel}
                </Card.Content>
            </Card>
        );

    }
}

const mapDispatchToProps = dispatch => {
    return {
        addSimilarityQuery: (queryItem) => dispatch({type:actionType.ADD_SIMILARITY_QUERY,payload:queryItem})
    }
};

export default withRouter(connect(null, mapDispatchToProps)(cardDeck));