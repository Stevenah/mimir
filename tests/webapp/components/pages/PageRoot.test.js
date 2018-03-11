import React from 'react';
import PageRoot from '../../../../webapp/components/pages/PageRoot'
import renderer from 'react-test-renderer';

let wrapper;

test('PageRoot does render', () => {
    wrapper = shallow(
        <PageRoot>

        </PageRoot>
    );
    expect(wrapper).toMatchSnapshot();
});
