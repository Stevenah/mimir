import React from 'react';
import ImageAttachment from '../../../../webapp/components/ui/ImageAttachment'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'
 
const mockStore = configureStore();

let store;
let wrapper;

test('ImageAttachment does render', () => {
  const wrapper = shallow(
      <ImageAttachment store={mockStore(initialState)}>This is a test!</ImageAttachment>
  );
  expect(wrapper).toMatchSnapshot();
});
