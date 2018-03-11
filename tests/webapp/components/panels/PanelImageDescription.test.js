import React from 'react';
import PanelImageDescription from '../../../../webapp/components/panels/PanelImageDescription'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'
 
const mockStore = configureStore();

let store;
let wrapper;

test('PanelImageDescription does render', () => {
  const wrapper = shallow(
      <PanelImageDescription store={mockStore(initialState)}>This is a test!</PanelImageDescription>
  );
  expect(wrapper).toMatchSnapshot();
});
