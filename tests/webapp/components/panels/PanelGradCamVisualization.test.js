import React from 'react';
import PanelGradCamVisualization from '../../../../webapp/components/panels/PanelGradCamVisualization'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'
 
const mockStore = configureStore();

let store;
let wrapper;

test('PanelGradCamVisualization does render', () => {
  const wrapper = shallow(
      <PanelGradCamVisualization store={mockStore(initialState)}>This is a test!</PanelGradCamVisualization>
  );
  expect(wrapper).toMatchSnapshot();
});
