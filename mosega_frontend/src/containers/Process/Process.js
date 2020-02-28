import React, {Component} from 'react';
import { Grid, Menu, Segment } from 'semantic-ui-react';

import Similarity from '../../components/ProcessMain/Similarity/Similarity';
import Cluster from '../../components/ProcessMain/Cluster/Cluster';

class Process extends Component{

    state = { activeItem: 'similarity' };

    handleItemClick = (e, { name }) => this.setState({ activeItem: name });

    render() {

        const { activeItem } = this.state;

        return(
            <Grid>
                <Grid.Column width={4}>
                    <Menu fluid vertical tabular size='massive'>
                        <Menu.Item
                            name='similarity'
                            active={activeItem === 'similarity'}
                            onClick={this.handleItemClick}
                        />
                        <Menu.Item
                            name='cluster'
                            active={activeItem === 'cluster'}
                            onClick={this.handleItemClick}
                        />
                    </Menu>
                </Grid.Column>

                <Grid.Column stretched width={12} >
                    <Segment style={{"height":"90vh", marginRight: "10px", marginBottom:"10px"}}>
                        {this.state.activeItem ==='similarity' ? <Similarity/> : null }
                        {this.state.activeItem ==='cluster' ? <Cluster/> : null }
                    </Segment>
                </Grid.Column>
            </Grid>
        );
    }
}

export default Process;