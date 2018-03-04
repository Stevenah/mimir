import React, { Component } from 'react';
import classnames from 'classnames';
import { compose, withState, withHandlers } from 'recompose';

import 'style/ui/TextBox.scss';

const defaultClassNames = [
    'text-boxcontainer',
    'input-group',
];

class TextBox extends Component {
    
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
                <label style={{display: 'block', textAlign: 'left'}}>
                    {this.props.label}
                </label>
                <div className={'text-box'} 
                    contentEditable={true}
                    style={{width: '100%'}}
                    onInput={this.props.onChange}
                >
                    {this.props.value}
                </div>
            </div>
        )
    }
}

export default TextBox;