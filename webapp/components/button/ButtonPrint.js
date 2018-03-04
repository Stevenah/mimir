import React, { Component } from 'react';
import classnames from 'classnames';

import ButtonAction from 'components/button/ButtonAction'

class Buttonprint extends Component {

    static defaultProps = {
        classNames: [],
    }

    render() {
        <ButtonAction
            classNames={['print-button']}
        />
    }
}

export default ButtonAction;