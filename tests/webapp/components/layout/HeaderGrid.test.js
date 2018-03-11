import React from 'react';
import HeaderGrid from '../../../../webapp/components/layout/HeaderGrid'
import renderer from 'react-test-renderer';

let wrapper;

test('HeaderGrid does render', () => {
    wrapper = shallow(
        <HeaderGrid>

        </HeaderGrid>
    );
    expect(wrapper).toMatchSnapshot();
});
