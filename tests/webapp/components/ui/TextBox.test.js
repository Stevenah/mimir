import React from 'react';
import TextBox from '../../../../webapp/components/ui/TextBox'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'
 
const mockStore = configureStore();

let store;
let wrapper;

test('TextBox does render', () => {
  const wrapper = shallow(
      <TextBox store={mockStore(initialState)}>This is a test!</TextBox>
  );
  expect(wrapper).toMatchSnapshot();
});
