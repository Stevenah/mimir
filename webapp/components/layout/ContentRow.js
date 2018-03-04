import React, { Component } from 'react';
import { Grid } from 'semantic-ui-react'

import 'style/layout/GridLayout.scss';

class ContentRow extends Component {
    render() {
        return (
            <Grid.Row className='grid-row'>
                {this.props.children}
            </Grid.Row>
        );
    }
}

export default ContentRow;