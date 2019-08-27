// export * from "./pizzas.reducer";
import * as fromPizzas from "./pizzas.reducer";
import { ActionReducerMap, createFeatureSelector } from "@ngrx/store";

// todo why these special export here instead  of *?
export interface ProductsState {
  pizzas: fromPizzas.PizzaState; //{loading;loaded;entities}
}

export const reducers: ActionReducerMap<ProductsState> = {
  pizzas: fromPizzas.reducer
};

export const getProductsState = createFeatureSelector<ProductsState>("ducks");
