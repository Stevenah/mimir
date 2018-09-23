import React, { Component } from 'react';

import 'style/layout/Grid.scss';

class Grid extends Component {
    
    static defaultProps = {
        children: []
    }
    
    static propTypes = {
        
    }

    render() {
        return (
            <div
                columns={this.props.children.length}
                className='grid-layout grid-content'
                verticalAlign='middle'
            >
                {this.props.children}
            </div>
        );
    }
}

export default Grid;