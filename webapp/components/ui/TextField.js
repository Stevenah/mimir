import React, { Component } from 'react';
import classnames from 'classnames';
import { compose, withState, withHandlers } from 'recompose';

import 'style/ui/TextField.scss';

const defaultClassNames = [
    'text-field-container',
];

class TextField extends Component {

    static defaultProps = {
        classNames: [],
        className: '',
    }

    shouldComponentUpdate(nextProps, nextState) {
        return this.props.value !== nextProps.value;
    }

    render() {

        let classNames = classnames(
            defaultClassNames,
            this.props.className,
        );

        return (
            <div className={classNames}>
                <label>
                    {this.props.label}
                </label>
                <input onChange={this.props.onChange}
                    type='text' 
                    value={this.props.value}
                />
            </div>
        );
    }
}


export default TextField;