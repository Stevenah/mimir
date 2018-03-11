import React from 'react';
import ButtonToggleAttachFile from '../../../../webapp/components/button/ButtonToggleAttachFile'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'

const mockStore = configureStore();

let store;
let wrapper;

test('ButtonToggleAttachFile does render', () => {
  const wrapper = shallow(
      <ButtonToggleAttachFile store={mockStore(initialState)}>
        This is a test!
      </ButtonToggleAttachFile>
  );
  expect(wrapper).toMatchSnapshot();
});
