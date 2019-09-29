import { TestBed } from "@angular/core/testing";
import { StoreModule, Store, combineReducers } from "@ngrx/store";

import * as fromRootReducers from "../../../app/store/reducers";
//^ why need this?
import * as fromReducers from "../reducers";
import * as fromActions from "../actions";
import * as fromSelectors from "../selectors/toppings.selector";
import { Topping } from "src/products/models/topping.model";

describe("Toppings selectors", () => {
  let store: Store<fromReducers.ProductsState>;
  const toppings: Topping[] = [
    { id: 1, name: "topping 1" },
    { id: 2, name: "topping 2" },
    { id: 3, name: "topping 3" }
  ];
  const entities = {
    1: toppings[0],
    2: toppings[1],
    3: toppings[2]
  };
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [
        StoreModule.forRoot({
          ...fromRootReducers.reducers,
          products: combineReducers(fromReducers.reducers)
        })
      ]
    });
    store = TestBed.get(Store); // lets us get a ref to the Store used here
    spyOn(store, "dispatch").and.callThrough(); // w/o call through method will get replaced
  });

  describe("getToppingEntities", () => {
    it("should return toppings as entities", () => {
      let result;
      store.select(fromSelectors.getToppingEntities).subscribe(value => {
        result = value;
      });
      expect(result).toEqual({});

      store.dispatch(new fromActions.LoadToppingsSuccess(toppings));
      expect(result).toEqual(entities); // result changes due to observable
    });
  });

  describe("getSelectedToppings", () => {
    it("should return selected toppings as ids", () => {
      let result;
      store.select(fromSelectors.getSelectedToppings).subscribe(value => {
        result = value;
      });
      store.dispatch(new fromActions.LoadToppingsSuccess(toppings));
      expect(result).toEqual([]); // initial result

      store.dispatch(new fromActions.VisualizeToppings([1, 3])); // this sets selected

      expect(result).toEqual([1, 3]); // result changes due to observable
    });
  });
});
