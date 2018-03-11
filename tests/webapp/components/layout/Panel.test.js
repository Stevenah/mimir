import React from 'react';
import Panel from '../../../../webapp/components/layout/Panel'
import renderer from 'react-test-renderer';

let wrapper;

test('Panel does render', () => {
    wrapper = shallow(
        <Panel>

        </Panel>
    );
    expect(wrapper).toMatchSnapshot();
});
