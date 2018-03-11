import React from 'react';
import Page from '../../../../webapp/components/ui/Page'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'
 
const mockStore = configureStore();

let store;
let wrapper;

test('Page does render', () => {
  const wrapper = shallow(
      <Page store={mockStore(initialState)}>This is a test!</Page>
  );
  expect(wrapper).toMatchSnapshot();
});
