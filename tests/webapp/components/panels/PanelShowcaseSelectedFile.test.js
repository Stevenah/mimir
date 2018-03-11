import React from 'react';
import PanelShowcaseSelectedFile from '../../../../webapp/components/panels/PanelShowcaseSelectedFile'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'

const mockStore = configureStore();

let store;
let wrapper;

test('PanelShowcaseSelectedFile does render', () => {
  const wrapper = shallow(
      <PanelShowcaseSelectedFile store={mockStore(initialState)}>This is a test!</PanelShowcaseSelectedFile>
  );
  expect(wrapper).toMatchSnapshot();
});
