import React, {Component} from 'react';
import classnames from 'classnames';

class SidebarMenuItem extends Component {
    render() {
        return (
            <li>
                { this.props.children }
            </li>
        )
    }
}

export default SidebarMenuItem;