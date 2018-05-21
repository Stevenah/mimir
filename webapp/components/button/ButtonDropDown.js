import React, { Component } from 'react';
import ButtonCover from 'components/button/ButtonCover';

import 'style/button/ButtonDropDown.scss';

class ButtonDropDown extends Component {
    
    static defaultProps = {
        classNames: [],
        options: { 'default': 'All' },
        selected: 0,
        listFunction: Function.prototype,
    }
    
    renderDropdown = () => {
        return Object.keys(this.props.options).map(optionId => (
            <li onClick={ () => this.props.onClick(optionId) }>
                { this.props.options[optionId] }
            </li>
        ));
    }

	render() {
        
		return (
            <div class="dropdown">
                <span>{this.props.options[this.props.selected]}</span>
                <div class="dropdown-content">
                    <ul>
                        {this.renderDropdown()}
                    </ul>
                </div>
            </div>
        )
	}
};

export default ButtonDropDown;