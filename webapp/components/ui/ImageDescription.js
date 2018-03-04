import React, { Component } from 'react';

import 'style/ui/ImageDescription.scss';

class ImageDescription extends Component {
    render() {
        return (
            <div className={'image-description'}>
                { this.props.description }            
            </div>
        );
    }
}

export default ImageDescription;