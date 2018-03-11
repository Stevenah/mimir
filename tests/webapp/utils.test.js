import { isEmpty } from '../../webapp/utils';

describe('isEmpty', () => {
    test('that empty object is true', () => {
        expect(isEmpty({})).toEqual(true)
    });
});