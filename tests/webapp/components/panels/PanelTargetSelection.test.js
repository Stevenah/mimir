import React from 'react';
import PanelTargetSelection from '../../../../webapp/components/panels/PanelTargetSelection'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'

const mockStore = configureStore();

let store;
let wrapper;

test('PanelTargetSelection does render', () => {
  const wrapper = shallow(
      <PanelTargetSelection store={mockStore(initialState)}>This is a test!</PanelTargetSelection>
  );
  expect(wrapper).toMatchSnapshot();
});
