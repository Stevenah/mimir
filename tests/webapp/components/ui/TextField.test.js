import React from 'react';
import TextField from '../../../../webapp/components/ui/TextField'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'
 
const mockStore = configureStore();

let store;
let wrapper;

test('TextField does render', () => {
  const wrapper = shallow(
      <TextField store={mockStore(initialState)}>This is a test!</TextField>
  );
  expect(wrapper).toMatchSnapshot();
});
