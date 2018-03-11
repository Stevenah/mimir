import React from 'react';
import ContentGrid from '../../../../webapp/components/layout/ContentGrid'
import renderer from 'react-test-renderer';

let wrapper;

test('ContentGrid does render', () => {
    wrapper = shallow(
        <ContentGrid>

        </ContentGrid>
    );
    expect(wrapper).toMatchSnapshot();
});
