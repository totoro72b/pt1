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
  constructor(public payload: any) {
    // this.payload = payload;
  }
}

export class LoadPizzasFail implements Action {
  readonly type = LOAD_PIZZAS_FAIL;
  constructor(public payload: Pizza[]) {
    // this.payload = payload; // todo apparently not necessary
  }
}

// action types
export type PizzasAction = LoadPizzas | LoadPizzasFail | LoadPizzasSuccess;
