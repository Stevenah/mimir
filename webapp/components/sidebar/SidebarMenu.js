import React, {Component} from 'react';
import classnames from 'classnames';

class SidebarMenu extends Component {
    render() {
        return (
            <ul>
                { this.props.children }
            </ul>
        );
    }
}

export default SidebarMenu;