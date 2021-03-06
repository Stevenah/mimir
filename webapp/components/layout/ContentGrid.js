import React, { Component } from 'react';
import { Grid } from 'semantic-ui-react';

import 'style/layout/GridLayout.scss';

class ContentGrid extends Component {
    
    static defaultProps = {
        children: []
    }

    render() {
        return (
            <Grid 
                columns={this.props.children.length}
                className='grid-layout grid-content'
                verticalAlign='middle'
            >
                {this.props.children}
            </Grid>
        );
    }
}

export default ContentGrid;