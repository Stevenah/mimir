import React, { Component } from 'react';
import classnames from 'classnames';

import 'style/ui/ImageAttachment.scss'

const defaultClasses = [
    'ui-image-attachment-container',
];

class ImageAttachment extends Component {

    static defaultProps = {
        classNames: []
    }

    render() {

        const classNames = classnames(
            defaultClasses,
            this.props.classNames,
        );

        return (
            <div className={classNames}>
                <span className='ui-image-attachment-label'>
                    { this.props.label }
                </span>
                <img className='ui-image-attachment' src={this.props.src} /> 
            </div>
        );
    }
}

export default ImageAttachment;