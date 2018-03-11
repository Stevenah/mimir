import React from 'react';
import ButtonDetachFile from '../../../../webapp/components/button/ButtonDetachFile'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'

const mockStore = configureStore();

let store;
let wrapper;

test('ButtonDetachFile does render', () => {
  const wrapper = shallow(
      <ButtonDetachFile store={mockStore()}>This is a test!</ButtonDetachFile>
  );
  expect(wrapper).toMatchSnapshot();
});
