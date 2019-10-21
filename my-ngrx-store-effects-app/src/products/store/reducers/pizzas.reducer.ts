import * as pizzaActions from "../actions/pizzas.action";
import { Pizza } from "src/products/models/pizza.model";

export interface PizzaState {
  entities: { [id: number]: Pizza };
  loaded: boolean;
  loading: boolean;
}
export const initialState: PizzaState = {
  entities: {},
  loaded: false,
  loading: false
};

export function reducer(
  state = initialState,
  action: pizzaActions.PizzasAction
): PizzaState {
  console.log("pizza action", action);
  switch (action.type) {
    case pizzaActions.LOAD_PIZZAS: {
      return { ...state, loaded: false, loading: true };
    }
    case pizzaActions.LOAD_PIZZAS_FAIL: {
      return { ...state, loaded: false, loading: false };
    }
    case pizzaActions.LOAD_PIZZAS_SUCCESS: {
      // add freshly loaded pizzas to our store
      const pizzas: Pizza[] = action.payload;
      const reducer = (accu: { [id: number]: Pizza }, curVal: Pizza) => {
        return { ...accu, [curVal.id]: curVal };
      };
      const newEntities: { [id: number]: Pizza } = pizzas.reduce(
        reducer,
        state.entities
      );

      return { ...state, loaded: true, loading: false, entities: newEntities };
    }

    // update and create share code
    case pizzaActions.UPDATE_PIZZA_SUCCESS:
    case pizzaActions.CREATE_PIZZA_SUCCESS: {
      const pizza = action.payload;
      const entities = {
        ...state.entities,
        [pizza.id]: pizza
      };
      return { ...state, entities };
    }
    case pizzaActions.REMOVE_PIZZA_SUCCESS: {
      const pizza = action.payload;
      // const entities = Object.keys(state.entities)
      //   .filter(id => id != pizza.id) // double equal here for string and int comparision
      //   .reduce((acc, id) => {
      //     return { ...acc, [id]: state.entities[parseInt(id, 10)] };
      //   }, state.entities);
      // wow objects destructuring
      const { [pizza.id]: removed, ...entities } = state.entities;
      return { ...state, entities };
    }
  }
  // return state as is on unrecognized actions
  return state;
}

// todo why isn't this exported in reducers/index.ts like the rest?
// because we don't want to introduce these into the module level
// checkout pizzas.selector.ts, where it imports using 2 different levels as the follows
// import * as fromFeature from "../reducers";
// import * as fromPizzas from "../reducers/pizzas.reducer";

export const getPizzasEntities = (state: PizzaState) => state.entities;
export const getPizzasLoading = (state: PizzaState) => state.loading;
export const getPizzasLoaded = (state: PizzaState) => state.loaded;
