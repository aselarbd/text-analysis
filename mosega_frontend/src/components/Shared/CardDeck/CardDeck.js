import React, {Component} from 'react';
import {Button, Card, Select, Input} from 'semantic-ui-react';
import {withRouter} from 'react-router-dom';
import {connect} from 'react-redux';
import * as actionType from '../../../store/action';


const options = [
    { key: 'a', text: 'Three', value: 3 },
    { key: 'b', text: 'Five', value: 5 },
    { key: 'c', text: 'Ten', value: 10 }

];
class cardDeck extends Component{

    state={
        similarityTextBox:'',
        preClusterCount:null
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

    preClusterButtonHandler = () => {
        if (this.state.preClusterCount !=null){
            this.props.preClusterQuery({
                query:this.props.heading,
                queryType:this.props.displayType,
                noOfClusters:this.state.preClusterCount
            });
            this.props.history.push({
                pathname:"/pre-cluster",
            });
        }
    };

    preClusterCountHandler = (event, val) => {
        this.setState({preClusterCount:val.value});
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

                <Select style={{marginLeft: "20px", marginRight: "20px"}}
                        required
                        options={options}
                        onChange={this.preClusterCountHandler}
                        placeholder='Select pre cluster count'
                />
                <Button basic color='black'
                        size='large'
                        style={{marginLeft: "20px", marginRight: "20px"}}
                        onClick={this.preClusterButtonHandler}
                >Find the Cluster </Button>

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
        addSimilarityQuery: (queryItem) => dispatch({type:actionType.ADD_SIMILARITY_QUERY,payload:queryItem}),
        preClusterQuery: (queryItem) => dispatch({type:actionType.PRE_CLUSTER_QUERY,payload:queryItem})
    }
};

export default withRouter(connect(null, mapDispatchToProps)(cardDeck));