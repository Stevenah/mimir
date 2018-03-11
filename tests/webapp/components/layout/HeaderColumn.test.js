import React from 'react';
import HeaderColumn from '../../../../webapp/components/layout/HeaderColumn'
import renderer from 'react-test-renderer';

let wrapper;

test('HeaderColumn does render', () => {
    wrapper = shallow(
        <HeaderColumn>

        </HeaderColumn>
    );
    expect(wrapper).toMatchSnapshot();
});
