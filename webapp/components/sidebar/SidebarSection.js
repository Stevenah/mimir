import React, {Component} from 'react';
import classnames from 'classnames';

class SidebarSection extends Component {
    render() {
        return (
            <section>
                <header>
                    { this.props.title }
                </header>
                { this.props.children }
            </section>
        )
    }
}

export default SidebarSection;