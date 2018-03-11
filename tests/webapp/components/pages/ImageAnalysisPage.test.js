import React from 'react';
import ImageAnalysisPage from '../../../../webapp/components/pages/ImageAnalysisPage'
import renderer from 'react-test-renderer';

let wrapper;

test('ImageAnalysisPage does render', () => {
    wrapper = shallow(
        <ImageAnalysisPage>

        </ImageAnalysisPage>
    );
    expect(wrapper).toMatchSnapshot();
});
