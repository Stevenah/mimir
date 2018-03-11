import React from 'react';
import PanelReport from '../../../../webapp/components/panels/PanelReport'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'
 
const mockStore = configureStore();

let store;
let wrapper;

test('PanelReport does render', () => {
  const wrapper = shallow(
      <PanelReport store={mockStore(initialState)}>This is a test!</PanelReport>
  );
  expect(wrapper).toMatchSnapshot();
});
