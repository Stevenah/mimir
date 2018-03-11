import React from 'react';
import ColonoscopyReport from '../../../../webapp/components/ui/ColonoscopyReport'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'
 
const mockStore = configureStore();

let store;
let wrapper;

test('ColonoscopyReport does render', () => {
  const wrapper = shallow(
      <ColonoscopyReport store={mockStore(initialState)}>This is a test!</ColonoscopyReport>
  );
  expect(wrapper).toMatchSnapshot();
});
