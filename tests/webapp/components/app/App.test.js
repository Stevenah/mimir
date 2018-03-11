import React from 'react';
import App from '../../../../webapp/components/app/App'
import renderer from 'react-test-renderer';

test('App does render', () => {
  const wrapper = shallow(
      <App></App>
  );
  expect(wrapper).toMatchSnapshot();
});
