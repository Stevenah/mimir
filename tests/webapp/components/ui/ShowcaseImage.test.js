import React from 'react';
import ShowcaseImage from '../../../../webapp/components/ui/ShowcaseImage'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'
 
const mockStore = configureStore();

let store;
let wrapper;

test('ShowcaseImage does render', () => {
  const wrapper = shallow(
      <ShowcaseImage store={mockStore(initialState)}>This is a test!</ShowcaseImage>
  );
  expect(wrapper).toMatchSnapshot();
});
