import React from 'react';
import ImageDescription from '../../../../webapp/components/ui/ImageDescription'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'
 
const mockStore = configureStore();

let store;
let wrapper;

test('ImageDescription does render', () => {
  const wrapper = shallow(
      <ImageDescription store={mockStore(initialState)}>This is a test!</ImageDescription>
  );
  expect(wrapper).toMatchSnapshot();
});
