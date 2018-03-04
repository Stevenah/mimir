import React, { Component } from 'react';

import 'style/ui/ShowcaseImage.scss'

class ShowcaseImage extends Component {
    render() {
        return (
            <img className='selected-image'
                 src={ this.props.source }
            />
        );
    }
}

export default ShowcaseImage;