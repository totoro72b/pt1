export const initialState = {
  loading: false,
  loaded: false,
  data: [{ label: "eat pizza", complete: false }] // let reducer to provide initial state
};

export function reducer(
  // a generic reducer that odesn't need to know about todos
  state = initialState,
  action: { payload: any; type: string }
) {
  switch (action.type) {
    case "ADD_TODO":
      return {
        ...state, // preserve original properties
        data: [...state.data, action.payload]
      };
  }
  return state;
}
