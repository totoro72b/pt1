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
  }
  return initialState;
}

// todo why isn't this exported in reducers/index.ts like the rest?
export const getPizzasEntities = (state: PizzaState) => state.entities;
export const getPizzasLoading = (state: PizzaState) => state.loading;
export const getPizzasLoaded = (state: PizzaState) => state.loaded;
