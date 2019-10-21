import * as fromPizzas from "./pizzas.reducer";
import * as fromToppings from "./toppings.reducer";
import { ActionReducerMap, createFeatureSelector } from "@ngrx/store";

// todo why these special export here instead  of *?
export interface ProductsState {
  pizzas: fromPizzas.PizzaState; //{loading;loaded;entities}
  toppings: fromToppings.ToppingsState;
}

// add to this map here to register these reducers
// it's used in products.module.ts StoreModule.forFeature('products', reducers)
export const reducers: ActionReducerMap<ProductsState> = {
  pizzas: fromPizzas.reducer,
  toppings: fromToppings.reducer
};

// "products" string referenced in products.module.ts
// so all the states reduced by these reducers are under the key "products"
export const getProductsState = createFeatureSelector<ProductsState>(
  "products"
);
