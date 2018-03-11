import React from 'react';
import PanelGuidedGradCamVisualization from '../../../../webapp/components/panels/PanelGuidedGradCamVisualization'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'

const mockStore = configureStore();

let store;
let wrapper;

test('PanelGuidedGradCamVisualization does render', () => {
  const wrapper = shallow(
      <PanelGuidedGradCamVisualization store={mockStore(initialState)}>This is a test!</PanelGuidedGradCamVisualization>
  );
  expect(wrapper).toMatchSnapshot();
});
