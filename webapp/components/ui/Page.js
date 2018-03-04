import React, { Component } from 'react';
import classnames from 'classnames';

import 'style/ui/Page.scss'

const defaultClassNames = [
    'page',
];

class Page extends Component {
   
    static defaultProps = {
        classNames: [],
    }

    render() {
        let classNames = classnames(
            defaultClassNames,
            this.props.classNames,
        );

        return (
            <div className={classNames}>
                {this.props.children}
            </div>
        );
    }
}

export default Page;