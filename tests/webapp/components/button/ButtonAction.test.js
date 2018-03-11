import React from 'react';
import ButtonAction from '../../../../webapp/components/button/ButtonAction'
import renderer from 'react-test-renderer';

test('ButtonAction does render', () => {
  const wrapper = shallow(
      <ButtonAction>Hello Jest!</ButtonAction>
  );
  expect(wrapper).toMatchSnapshot();
});
