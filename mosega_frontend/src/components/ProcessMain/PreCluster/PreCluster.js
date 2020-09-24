import React, {Component} from 'react';
import axios from 'axios';
import * as URL from '../../../constants/URL';
import { Dimmer, Loader, Segment } from 'semantic-ui-react';
import {connect} from 'react-redux';
import Deck from "../../Shared/CardDeck/CardDeck";

class PreCluster extends Component{

    state = {
        clusterRes:null
    };

    componentDidMount() {
        const data = {
            "processType":"preCluster",
            "dataType":this.props.preClusterQueryType,
            "noOfClusters":this.props.preClusterCount,
            "headerTitle":this.props.preClusterQuery
        };
        axios.post(URL.PROCESSING,data)
            .then(resp => {
                this.setState({clusterRes:resp.data});
            });
    }

render() {

    let clusterResult = (
        <Segment style={{marginLeft: "10px", marginRight: "10px", marginTop: "30px", height:"400px"}}>
            <Dimmer active inverted>
                <Loader size='large'>Loading Clustering Results ...</Loader>
            </Dimmer>
        </Segment>
    );

    if(this.state.clusterRes != null){
        clusterResult = (
            this.state.clusterRes.map((item,index)=> (
                <Deck
                    key={'cluster_'+index}
                    heading={item.heading}
                    text={item.text}
                />
            ))
        );
    }

    return(
        <div>
            <div style={{marginTop:"30px"}}>
                <h2 style={{ textAlign: "center"}}>Pre Cluster Results ({this.props.preClusterCount})</h2>
                <br/>
            {clusterResult}
            </div>
        </div>
    );
}
}
const mapStateToProps = state => {
    return {
        preClusterCount: state.preCluster.noOfClusters,
        preClusterQuery: state.preCluster.query,
        preClusterQueryType: state.preCluster.queryType
    }
};
export default connect (mapStateToProps,null) (PreCluster);
