import React from 'react';
import SidebarMenuItem from '../../../../webapp/components/sidebar/SidebarMenuItem'
import renderer from 'react-test-renderer';

let wrapper;

test('SidebarMenuItem does render', () => {
    wrapper = shallow(
        <SidebarMenuItem>

        </SidebarMenuItem>
    );
    expect(wrapper).toMatchSnapshot();
});
