import React from 'react';
import ButtonUpload from '../../../../webapp/components/button/ButtonUpload'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'

const mockStore = configureStore();

let store;
let wrapper;

test('ButtonUpload does render', () => {
    wrapper = shallow(
        <ButtonUpload store={mockStore(initialState)} />
    );
    expect(wrapper).toMatchSnapshot();
});
