import React from 'react';
import FileSelector from '../../../../webapp/components/ui/FileSelector'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'
 
const mockStore = configureStore();

let store;
let wrapper;

test('FileSelector does render', () => {
  const wrapper = shallow(
      <FileSelector store={mockStore(initialState)}>This is a test!</FileSelector>
  );
  expect(wrapper).toMatchSnapshot();
});
