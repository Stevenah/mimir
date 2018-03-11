import React from 'react';
import SidebarMenu from '../../../../webapp/components/sidebar/SidebarMenu'
import renderer from 'react-test-renderer';

let wrapper;

test('SidebarMenu does render', () => {
    wrapper = shallow(
        <SidebarMenu>

        </SidebarMenu>
    );
    expect(wrapper).toMatchSnapshot();
});
