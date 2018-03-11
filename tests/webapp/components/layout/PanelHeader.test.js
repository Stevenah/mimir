import React from 'react';
import PanelHeader from '../../../../webapp/components/layout/PanelHeader'
import renderer from 'react-test-renderer';

let wrapper;

test('PanelHeader does render', () => {
    wrapper = shallow(
        <PanelHeader>

        </PanelHeader>
    );
    expect(wrapper).toMatchSnapshot();
});
