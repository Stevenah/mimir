import React, { Component } from 'react';
import classnames from 'classnames';

import 'style/button/ButtonAction.scss';

const defaultClasses = [
    'link-button',
    'analysis-header-button',
];

class ButtonAction extends Component {

    static defaultProps = {
        classNames: [],
    }

    render() {
        let classNames = classnames(
            defaultClasses,
            this.props.classNames,
        );

        let label = this.props.children ? 
            this.props.children : this.props.label;

        return (
            <span 
                className={classNames}
                onClick={this.props.onClick}
            >
                {label}
            </span>
        );
    }
}

export default ButtonAction;