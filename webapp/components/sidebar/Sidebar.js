import React, { Component } from 'react'
import { Link } from 'react-router-dom'

import SidebarSection from 'components/sidebar/SidebarSection';
import SidebarMenu from 'components/sidebar/SidebarMenu';
import SidebarMenuItem from 'components/sidebar/SidebarMenuItem';

import 'style/sidebar/SideBar.scss';

class Sidebar extends Component {
    render() {
        return (
            <nav className='sidebar'>
                <header>
                    Mímir
                </header>
                <SidebarSection title='Analysis and Reporting'>
                    <SidebarMenu>
                        <SidebarMenuItem>
                            <Link to='/image'>Image Analysis</Link>
                        </SidebarMenuItem>
                        <SidebarMenuItem>
                            <Link to='/report'>Reports</Link>
                        </SidebarMenuItem>
                    </SidebarMenu>
                </SidebarSection>
            </nav>
        )
    }
}

export default Sidebar;