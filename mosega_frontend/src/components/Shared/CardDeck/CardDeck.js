import React, {Component} from 'react';
import {Button, Card, Select, Input, Grid} from 'semantic-ui-react';
import {withRouter} from 'react-router-dom';
import {connect} from 'react-redux';
import * as actionType from '../../../store/action';
import * as Constants from '../../../constants/Constants';


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

    similarityTextHandler = () => {
        if (this.state.similarityTextBox !== ''){
            this.findSimilarity(this.state.similarityTextBox, this.props.displayType, Constants.PROCESSING_SIMILAR);
        }
    };

    similarityTopicHandler = () => {
        this.findSimilarity(this.props.heading, this.props.displayType, Constants.PROCESSING_SIMILAR);
    };

    similarityWholeHandler = () => {
        this.findSimilarity(this.props.text, this.props.displayType, Constants.PROCESSING_SIMILAR_WHOLE);
    };

    findSimilarity = (query, query_type, process_type) => {

        this.props.addSimilarityQuery({
            query:query,
            queryType:query_type,
            processType:process_type,
            itemID:this.props.itemID
        });

        this.props.history.push({
            pathname:"/process",
        });
    }

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
                <Grid columns='four' divided='vertically'>
                    <Grid.Row>
                        <Grid.Column>
                            <Button basic color='black' onClick={this.similarityTopicHandler}>
                                Find Similar clauses based on Topic
                            </Button>
                        </Grid.Column>
                        <Grid.Column>
                            <Button basic color='black' onClick={this.similarityWholeHandler}>
                                Find Similar clauses based on Full Content
                            </Button>
                        </Grid.Column>
                        <Grid.Column>
                            <Input style={{marginLeft: "20px", marginRight: "20px"}}
                                   size='large' icon='search'
                                   placeholder='Search Similarity phrases ...'
                                   value={this.state.similarityTextBox}
                                   onChange={this.similarityTextBoxHandler}
                            />
                        </Grid.Column>
                        <Grid.Column>
                            <Button basic color='black'
                                    size='large'
                                    onClick={this.similarityTextHandler}
                            >Search </Button>
                        </Grid.Column>
                    </Grid.Row>

                    <Grid.Row>
                        <Grid.Column>
                            <Select style={{marginLeft: "20px", marginRight: "20px"}}
                                    required
                                    options={options}
                                    onChange={this.preClusterCountHandler}
                                    placeholder='Select pre cluster count'
                            />
                        </Grid.Column>
                        <Grid.Column>
                            <Button basic color='black'
                                    size='large'
                                    style={{marginLeft: "20px", marginRight: "20px"}}
                                    onClick={this.preClusterButtonHandler}
                            >
                                Find the Cluster
                            </Button>
                        </Grid.Column>
                    </Grid.Row>
                </Grid>
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