import React from 'react';
import Sidebar from '../../../../webapp/components/sidebar/Sidebar'
import renderer from 'react-test-renderer';

let wrapper;

test('Sidebar does render', () => {
    wrapper = shallow(
        <Sidebar>

        </Sidebar>
    );
    expect(wrapper).toMatchSnapshot();
});
