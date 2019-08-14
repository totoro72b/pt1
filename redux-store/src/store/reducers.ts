import * as fromActions from './actions';

export const initialState = {
  loading: false,
  loaded: false,
  data: [{ label: 'eat pizza', complete: false }] // let reducer to provide initial state
};

export function reducer(
  // a generic reducer that doesn't need to know about todos
  state = initialState,
  action: { payload: any; type: string }
) {
  switch (action.type) {
    case fromActions.ADD_TODO:
      return {
        ...state, // preserve original properties
        data: [...state.data, action.payload]
      };
    case fromActions.REMOVE_TODO: {
      const data = state.data.filter(
        todo => todo.label !== action.payload.label
      );
      return {
        ...state,
        data
      };
    }
  }
  return state;
}
