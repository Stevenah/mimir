import React, { Component } from 'react';
import classnames from 'classnames';

import 'style/ui/Image.scss';

const defaultClassNames = [
    'ui-image',
];

class Image extends Component {

    static defaultProps = {
        source: '',
        label: '',
        width: 100,
        height: 100,
        classNames: [],
        clickable: false,
        attached: false,
        selected: false,
        loading: false,
        onClick: Function.prototype,
    }

    render() {
        const classNames = classnames(
            defaultClassNames,
            this.props.classNames,
            {
                'ui-image-clickable': this.props.clickable,
                'ui-image-highlight-attached': this.props.attached,
                'ui-image-highlight-selected': this.props.selected,
            }
        );

        if (this.props.loading) {
            return (
                <div className={classNames} onClick={this.props.onClick}>
                    <img src={this.props.src}
                        width={this.props.width}
                        height={this.props.height}/>
                    <div className='ui active dimmer'>
                        <div className='ui loader'/>
                    </div>
                </div>
            );
        }
        
        return (
            <div className={classNames} onClick={this.props.onClick}>
                <img src={this.props.src}
                     width={this.props.width}
                     height={this.props.height}/>
                {this.props.label ?
                    <span className='ui-image-label-overlay'>
                        <span className='ui-image-label'>
                            {this.props.label}
                        </span>
                    </span>
                : ''}
                
            </div>
        );
    }
}

export default Image;