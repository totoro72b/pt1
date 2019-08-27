import { createSelector } from "@ngrx/store";
import * as fromRoot from "../../../app/store";
import * as fromFeature from "../reducers";
import * as fromPizzas from "../reducers/pizzas.reducer";
import { Pizza } from "src/products/models/pizza.model";

// TODO why pizzas filehere?
// equivalent as
// import * as fromFeature from "../reducers/index";

export const getPizzaState = createSelector(
  fromFeature.getProductsState,
  (state: fromFeature.ProductsState) => {
    console.log("get products state", state);
    return state.pizzas;
  }
);

export const getPizzasEntities = createSelector(
  getPizzaState,
  fromPizzas.getPizzasEntities
);

export const getSelectedPizza = createSelector(
  getPizzasEntities,
  fromRoot.getRouterState,
  (entities, router): Pizza => {
    // pass in current id from teh router state
    // todo what if router.state is falsy?
    const result = router.state && entities[router.state.params.pizzaId];
    console.log("router.state=", router.state, "result=", result);
    return router.state && entities[router.state.params.pizzaId];
  }
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
