import { createSelector } from "@ngrx/store";
import * as fromRoot from "../../../app/store";
import * as fromFeature from "../reducers";
// equivalent to
// import * as fromFeature from "../reducers/index";
import * as fromPizzas from "../reducers/pizzas.reducer";
import * as fromToppings from "./toppings.selector";
import { Pizza } from "src/products/models/pizza.model";
import { PizzaDisplayComponent } from "src/products/components";

// TODO why pizzas filehere?

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
    // todo what if router.state is falsy?
    const result = router.state && entities[router.state.params.pizzaId];
    console.log("get selected pizza result", result);
    return result;
  }
);

// todo what type does createSelector take? how does it know when it's selectors when funcs?
// compose a new selector from existing ones
export const getPizzaVisualized = createSelector(
  getSelectedPizza,
  fromToppings.getToppingEntities,
  fromToppings.getSelectedToppings,
  (pizza, toppingEntities, selectedToppings) => {
    const toppings = selectedToppings.map(id => toppingEntities[id]);
    return { ...pizza, toppings };
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
