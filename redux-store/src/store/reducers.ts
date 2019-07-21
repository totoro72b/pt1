export const initialState = {
  loading: false,
  loaded: false,
  data: [{ label: "asdf", complete: false }]
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
}

// function reduce(state, action){
//     switch(action.type){
//         'ADD_TODO':{
//             return {
//                 ...state,
//                 todos: [...state.todos, action.payload]
//             }
//         }
//     }
// }
// export reducers: Function[] =[reduce ];
