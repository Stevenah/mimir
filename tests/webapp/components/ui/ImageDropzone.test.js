import React from 'react';
import ImageDropzone from '../../../../webapp/components/ui/ImageDropzone'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'
 
const mockStore = configureStore();

let store;
let wrapper;

test('ImageDropzone does render', () => {
  const wrapper = shallow(
      <ImageDropzone store={mockStore(initialState)}>This is a test!</ImageDropzone>
  );
  expect(wrapper).toMatchSnapshot();
});
