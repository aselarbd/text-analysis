import React, {Component} from 'react';
import axios from 'axios';
import * as URL from '../../../constants/URL';
import {Dimmer, Divider, Loader, Segment} from 'semantic-ui-react';
import {connect} from 'react-redux';
import Deck from "../../Shared/CardDeck/CardDeck";
import classes from "./SimilaritySet.css";

class SimilaritySet extends Component{

    state = {
        similaritySetRes:null
    };

    componentDidMount() {
        const data = {
            "processType":"similaritySet",
            "dataType":this.props.similaritySetQueryType,
            "ID":this.props.similaritySetID
        };
        axios.post(URL.PROCESSING,data)
            .then(resp => {
                this.setState({similaritySetRes:resp.data});
            });
    }

    render() {

        let similaritySetResult = (
            <Segment style={{marginLeft: "10px", marginRight: "10px", marginTop: "30px", height:"400px"}}>
                <Dimmer active inverted>
                    <Loader size='large'>Loading Similarity Results ...</Loader>
                </Dimmer>
            </Segment>
        );

        if(this.state.similaritySetRes != null){
            let outerResult = [];
            for(let i=0; i< this.state.similaritySetRes.length; i++){
                outerResult.push
                    (
                        <div key={'outer_heading_'+i}>
                            <Divider horizontal style={{marginLeft:"10px", marginRight:"10px"}} >
                                {this.state.similaritySetRes[i].heading}
                            </Divider>
                            <br/>
                            <div className={classes.SimilaritySetResult}>
                                {this.state.similaritySetRes[i].similarSet.map((item,index) => (
                                    <div key={i+'_similar_part_'+index}>
                                        <Divider horizontal style={{marginLeft:"10px", marginRight:"10px"}}> {index + 1}</Divider>
                                        <br/>
                                        <Deck
                                            heading={item.heading}
                                            text={item.text}
                                            meta={'Accuracy : '+item.accuracy.toFixed(4)}
                                        />
                                        <br/>
                                    </div>

                                ))}
                            </div>
                            <br/>
                        </div>
                    )
            }
            similaritySetResult = outerResult;
        }

        return(
            <div>
                <div style={{marginTop:"30px"}}>
                    <Divider horizontal style={{marginLeft:"10px", marginRight:"10px", marginTop:"20px"}}>
                        Similarity Set Results
                    </Divider>
                    <br/>
                    {similaritySetResult}
                </div>
            </div>
        );
    }
}
const mapStateToProps = state => {
    return {
        similaritySetID: state.similaritySet.ID,
        similaritySetQueryType: state.similaritySet.queryType
    }
};
export default connect (mapStateToProps,null) (SimilaritySet);
