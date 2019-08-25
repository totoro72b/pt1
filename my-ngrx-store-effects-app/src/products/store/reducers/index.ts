// export * from "./pizzas.reducer";
import * as fromPizzas from "./pizzas.reducer";
import {
  ActionReducerMap,
  createFeatureSelector,
  createSelector
} from "@ngrx/store";

// todo why these special export here instead  of *?
export interface ProductsState {
  pizzas: fromPizzas.PizzaState; //{loading;loaded;entities}
}

export const reducers: ActionReducerMap<ProductsState> = {
  pizzas: fromPizzas.reducer
};

//todo why string products?
// todo: understand createFeatureSelector
// how the store is created and initial stuff is loaded?
export const getProductsState = createFeatureSelector<ProductsState>("ducks");

export const getPizzaState = createSelector(
  getProductsState,
  (state: ProductsState) => {
    console.log("get products state", state);
    return state.pizzas;
  }
);

export const getPizzasEntities = createSelector(
  getPizzaState,
  fromPizzas.getPizzasEntities
);

// get all the pizzas in an array
export const getAllPizzas = createSelector(
  getPizzasEntities,
  entities => {
    return Object.keys(entities).map(id => entities[parseInt(id, 10)]);
  }
);

export const getPizzasLoaded = createSelector(
  getPizzaState,
  fromPizzas.getPizzasLoaded
);

export const getPizzasLoading = createSelector(
  getPizzaState,
  fromPizzas.getPizzasLoading
);
