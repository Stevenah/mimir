import React from 'react';
import Image from '../../../../webapp/components/ui/Image'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'
 
const mockStore = configureStore();

let store;
let wrapper;

test('Image does render', () => {
  const wrapper = shallow(
      <Image store={mockStore(initialState)}>This is a test!</Image>
  );
  expect(wrapper).toMatchSnapshot();
});
