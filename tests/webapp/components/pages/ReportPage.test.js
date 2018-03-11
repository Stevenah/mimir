import React from 'react';
import ReportPage from '../../../../webapp/components/pages/ReportPage'
import renderer from 'react-test-renderer';

let wrapper;

test('ReportPage does render', () => {
    wrapper = shallow(
        <ReportPage>

        </ReportPage>
    );
    expect(wrapper).toMatchSnapshot();
});
