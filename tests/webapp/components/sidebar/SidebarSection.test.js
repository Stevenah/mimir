import React from 'react';
import SidebarSection from '../../../../webapp/components/sidebar/SidebarSection'
import renderer from 'react-test-renderer';

let wrapper;

test('SidebarSection does render', () => {
    wrapper = shallow(
        <SidebarSection>

        </SidebarSection>
    );
    expect(wrapper).toMatchSnapshot();
});
