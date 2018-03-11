import React from 'react';
import PanelLayerSelection from '../../../../webapp/components/panels/PanelLayerSelection'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'

const mockStore = configureStore();

let store;
let wrapper;

test('PanelLayerSelection does render', () => {
  const wrapper = shallow(
      <PanelLayerSelection store={mockStore(initialState)}>This is a test!</PanelLayerSelection>
  );
  expect(wrapper).toMatchSnapshot();
});
