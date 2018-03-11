import React from 'react';
import TableSelector from '../../../../webapp/components/ui/TableSelector'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'
 
const mockStore = configureStore();

let store;
let wrapper;

test('TableSelector does render', () => {
  const wrapper = shallow(
      <TableSelector store={mockStore(initialState)}>This is a test!</TableSelector>
  );
  expect(wrapper).toMatchSnapshot();
});
