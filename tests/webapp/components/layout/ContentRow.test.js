import React from 'react';
import ContentRow from '../../../../webapp/components/layout/ContentRow'
import renderer from 'react-test-renderer';

let wrapper;

test('ContentRow does render', () => {
    wrapper = shallow(
        <ContentRow>

        </ContentRow>
    );
    expect(wrapper).toMatchSnapshot();
});
