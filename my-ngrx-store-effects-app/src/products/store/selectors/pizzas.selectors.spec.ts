import { StoreModule, Store, combineReducers } from "@ngrx/store";
import { ROUTER_NAVIGATION } from "@ngrx/router-store";

import { TestBed } from "@angular/core/testing";
import { Pizza } from "../../models/pizza.model";

import * as fromRoot from "../../../app/store";
import * as fromReducers from "../reducers/index";
import * as fromActions from "../actions/index";
import * as fromSelectors from "../selectors/pizzas.selector";
import { iterateListLike } from "@angular/core/src/change_detection/change_detection_util";

describe("Pizzas Selectors", () => {
  let store: Store<fromReducers.ProductsState>;

  const pizza1: Pizza = {
    id: 1,
    name: "Fish 'n Chips",
    toppings: [{ id: 1, name: "fish" }, { id: 2, name: "chips" }]
  };

  const pizza2: Pizza = {
    id: 2,
    name: "Aloha",
    toppings: [{ id: 2, name: "pineapple" }, { id: 3, name: "cheese" }]
  };

  const pizza3: Pizza = {
    id: 3,
    name: "Burrito",
    toppings: [{ id: 4, name: "cheese" }, { id: 5, name: "avocado" }]
  };

  const pizzas: Pizza[] = [pizza1, pizza2, pizza3];

  const entities = {
    1: pizzas[0],
    2: pizzas[1],
    3: pizzas[2]
  };

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [
        StoreModule.forRoot({
          ...fromRoot.reducers,
          products: combineReducers(fromReducers.reducers)
        })
      ]
    });

    store = TestBed.get(Store);
  });
  describe("getPizzaState", () => {
    it("should return state of pizza store slice", () => {
      let result;
      store.select(fromSelectors.getPizzaState).subscribe(value => {
        result = value;
      });
      expect(result).toEqual({
        entities: {},
        loading: false,
        loaded: false
      });
      // dispatch an action and see that selector grab updated stuff
      store.dispatch(new fromActions.LoadPizzasSuccess(pizzas));
      //TODO: why is this synchronous test? looks async

      expect(result).toEqual({
        entities: entities,
        loaded: true,
        loading: false
      });
    });
  });

  describe("getSelectedPizza", () => {
    it("should return selected pizza as an entity", () => {
      let result;
      let params;
      store.dispatch(new fromActions.LoadPizzasSuccess(pizzas));

      store.dispatch({
        type: "ROUTER_NAVIGATION",
        payload: {
          routerState: {
            url: "/products/2",
            queryParams: {},
            params: {
              pizzaId: "2"
            }
          },
          event: {}
        }
      });
      // select state params
      store.select(fromRoot.getRouterState).subscribe(routerState => {
        params = routerState.state.params;
      });
      expect(params).toEqual({ pizzaId: "2" });

      // selected pizza selector depends on 1) pizza entities AND 2) router state
      // we setup 1) via LoadPizzasSuccess and 2) via store.dispatch({type: ROUTER_NAVIGATION...})
      // ROUTER_NAVIGATION is not defined by us; rahter it's from '@ngrx/router-store';

      store.select(fromSelectors.getSelectedPizza).subscribe(selectedPizza => {
        result = selectedPizza;
      });
      expect(result).toEqual(entities[2]);
    });
  });
});
