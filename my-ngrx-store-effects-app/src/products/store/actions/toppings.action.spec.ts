import * as fromToppings from "./toppings.action";

describe("Topping Actions", () => {
  it("should create LoadToppingActions", () => {
    const action = new fromToppings.LoadToppings();
    expect({ ...action }).toEqual({ type: fromToppings.LOAD_TOPPINGS });
  });
  // the other very similar to pizza actions tests.
});
