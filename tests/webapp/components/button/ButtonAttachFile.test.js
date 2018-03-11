import React from 'react';
import ButtonAttachFile from '../../../../webapp/components/button/ButtonAttachFile'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'

const mockStore = configureStore();

let store;
let wrapper;

test('ButtonAttachFile does render', () => {
  const wrapper = shallow(
      <ButtonAttachFile store={mockStore()}>This is a test!</ButtonAttachFile>
  );
  expect(wrapper).toMatchSnapshot();
});
