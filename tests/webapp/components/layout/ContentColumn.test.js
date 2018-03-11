import React from 'react';
import ContentColumn from '../../../../webapp/components/layout/ContentColumn'
import renderer from 'react-test-renderer';

let wrapper;

test('ContentColumn does render', () => {
    wrapper = shallow(
        <ContentColumn>

        </ContentColumn>
    );
    expect(wrapper).toMatchSnapshot();
});
