import { Action } from "@ngrx/store";
import { Pizza } from "src/products/models/pizza.model";

// load pizza actions
export const LOAD_PIZZAS: string = "[Pizza Action] Load Pizzas";
export const LOAD_PIZZAS_SUCCESS: string = "[Pizza Action] Load Pizzas success";
export const LOAD_PIZZAS_FAIL: string = "[Pizza Action] Load Pizzas fail";

export class LoadPizzas implements Action {
  readonly type = LOAD_PIZZAS;
  // todo shouldn't need this
  constructor(public payload: any) {}
}

// dispatched by effects after service returns
export class LoadPizzasSuccess implements Action {
  readonly type = LOAD_PIZZAS_SUCCESS;
  constructor(public payload: Pizza[]) {
    // this.payload = payload;
  }
}

export class LoadPizzasFail implements Action {
  readonly type = LOAD_PIZZAS_FAIL;
  constructor(public payload: any) {
    // this.payload = payload; // todo apparently not necessary
  }
}

// create pizza
export const CREATE_PIZZA = "[Products] Create Pizza";
export const CREATE_PIZZA_FAIL = "[Products] Create Pizza Fail";
export const CREATE_PIZZA_SUCCESS = "[Products] Create Pizza Success";

export class CreatePizza implements Action {
  readonly type = CREATE_PIZZA;
  constructor(public payload: Pizza) {}
}

export class CreatePizzaSuccess implements Action {
  readonly type = CREATE_PIZZA_SUCCESS;
  constructor(public payload: Pizza) {}
}

export class CreatePizzaFail implements Action {
  readonly type = CREATE_PIZZA_FAIL;
  constructor(public payload: any) {}
}

// update pizza
export const UPDATE_PIZZA = "[Products] Update Pizza";
export const UPDATE_PIZZA_FAIL = "[Products] Update Pizza Fail";
export const UPDATE_PIZZA_SUCCESS = "[Products] Update Pizza Success";

export class UpdatePizza implements Action {
  readonly type = UPDATE_PIZZA;
  constructor(public payload: Pizza) {}
}

export class UpdatePizzaSuccess implements Action {
  readonly type = UPDATE_PIZZA_SUCCESS;
  constructor(public payload: Pizza) {}
}

export class UpdatePizzaFail implements Action {
  readonly type = UPDATE_PIZZA_FAIL;
  constructor(public payload: any) {}
}

// remove pizza
export const REMOVE_PIZZA = "[Products] Remove Pizza";
export const REMOVE_PIZZA_FAIL = "[Products] Remove Pizza Fail";
export const REMOVE_PIZZA_SUCCESS = "[Products] Remove Pizza Success";

export class RemovePizza implements Action {
  readonly type = REMOVE_PIZZA;
  constructor(public payload: Pizza) {}
}
export class RemovePizzaFail implements Action {
  readonly type = REMOVE_PIZZA_FAIL;
  constructor(public payload: any) {}
}
export class RemovePizzaSuccess implements Action {
  readonly type = REMOVE_PIZZA_SUCCESS;
  constructor(public payload: Pizza) {} // hmm success removal also returns the pizza?
}

// action types
export type PizzasAction =
  | LoadPizzas
  | LoadPizzasFail
  | LoadPizzasSuccess
  | CreatePizza
  | CreatePizzaFail
  | CreatePizzaSuccess
  | UpdatePizza
  | UpdatePizzaFail
  | UpdatePizzaSuccess
  | RemovePizza
  | RemovePizzaFail
  | RemovePizzaSuccess;
