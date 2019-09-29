import * as fromPizzas from "./pizzas.action";

describe("Pizzas Actions", () => {
  describe("LoadPizzas Actions", () => {
    describe("LoadPizzas", () => {
      it("should create an action", () => {
        const action = new fromPizzas.LoadPizzas(null);
        expect({ ...action }).toEqual({
          type: fromPizzas.LOAD_PIZZAS,
          payload: null
        });
      });
    });
    describe("LoadPizzasFail", () => {
      it("should create an action", () => {
        const payload = { errors: "failed" };
        const action = new fromPizzas.LoadPizzasFail(payload);
        expect({ ...action }).toEqual({
          type: fromPizzas.LOAD_PIZZAS_FAIL,
          payload: payload
        });
      });
    });
    describe("LoadPizzasSuccess", () => {
      it("should create an action", () => {
        const pizza = {
          name: "Blazin' Inferno",
          toppings: [{ id: 10, name: "pepperoni" }, { id: 9, name: "pepper" }],
          id: 1
        };
        const pizza2 = {
          name: "Blazin' Inferno",
          toppings: [{ id: 10, name: "pepperoni" }, { id: 9, name: "pepper" }],
          id: 2
        };
        const action = new fromPizzas.LoadPizzasSuccess([pizza, pizza2]);
        expect({ ...action }).toEqual({
          type: fromPizzas.LOAD_PIZZAS_SUCCESS,
          payload: [pizza, pizza2]
        });
      });
    });
  });
});
