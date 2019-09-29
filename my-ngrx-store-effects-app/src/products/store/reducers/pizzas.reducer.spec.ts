import * as fromReducers from "./pizzas.reducer";
import * as fromActions from "../actions/pizzas.action";
import { iterateListLike } from "@angular/core/src/change_detection/change_detection_util";

// goal: initial state, action-> test new state
describe("Test Pizza Reducers", () => {
  const initialState = fromReducers.initialState;
  describe("test unmatched actions", () => {
    const state = { ...fromReducers.initialState, loaded: true };
    it("should return original state on unmatched action types", () => {
      const newState = fromReducers.reducer(state, {
        type: "_",
        payload: null
      });
      expect(newState).toEqual({ ...state });
    });
  });
  describe("test load pizzas", () => {
    const action = new fromActions.LoadPizzas(null);
    it("should change loading status when initial state passed as undefined", () => {
      const newState = fromReducers.reducer(undefined, action);
      expect(newState).toEqual({ ...initialState, loading: true });
    });
    it("should change loading status when initial state defined ", () => {
      const newState = fromReducers.reducer(
        { ...initialState, loading: false },
        action
      );
      expect(newState).toEqual({ ...initialState, loading: true });
    });
  });
  describe("test load pizzas fail reducer", () => {
    const action = new fromActions.LoadPizzasFail(null);
    it("should change loading status when initial state defined ", () => {
      const newState = fromReducers.reducer(
        { ...initialState, loading: true, loaded: true },
        action
      );
      expect(newState).toEqual({
        ...initialState,
        loading: false,
        loaded: false
      });
    });
  });
  describe("load pizza success", () => {
    it("should generate entities correctly", () => {
      const pizza1 = {
        name: "Blazin' Inferno",
        toppings: [{ id: 10, name: "pepperoni" }, { id: 9, name: "pepper" }],
        id: 1
      };
      const pizza2 = {
        name: "Blazin' Inferno",
        toppings: [{ id: 10, name: "pepperoni" }, { id: 9, name: "pepper" }],
        id: 2
      };
      const expectedEntities = {
        1: pizza1,
        2: pizza2
      };
      const payload = [pizza1, pizza2];
      const action = new fromActions.LoadPizzasSuccess(payload);
      const newState = fromReducers.reducer({ ...initialState }, action);
      expect(newState).toEqual({
        ...initialState,
        entities: expectedEntities,
        loaded: true
      });
    });
  });
  describe("test selectors in reducers", () => {
    it("should get entities ok", () => {
      const state = {
        ...initialState,
        entities: { 1: { name: "asdf", id: 1 } }
      };
      const slice = fromReducers.getPizzasEntities(state);
      expect({ ...slice }).toEqual({ 1: { id: 1, name: "asdf" } });
    });
  });
});
