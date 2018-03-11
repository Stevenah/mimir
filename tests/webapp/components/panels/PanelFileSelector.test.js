import React from 'react';
import PanelFileSelector from '../../../../webapp/components/panels/PanelFileSelector'
import renderer from 'react-test-renderer';
import configureStore from 'redux-mock-store'
 
const mockStore = configureStore();

let store;
let wrapper;

test('PanelFileSelector does render', () => {
  const wrapper = shallow(
      <PanelFileSelector store={mockStore(initialState)}>This is a test!</PanelFileSelector>
  );
  expect(wrapper).toMatchSnapshot();
});
