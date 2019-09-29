import { PizzasGuard } from "./pizzas.guard"; // import this guy so we could use it in the guards variable
import { PizzasExistGuard } from "./pizzas-exist.guard"; // import this guy so we could use it in the guards variable
import { PizzaToppingsGuard } from "./pizza-toppings.guard";
export const guards: any[] = [
  PizzasGuard,
  PizzasExistGuard,
  PizzaToppingsGuard
];

export * from "./pizzas.guard";
export * from "./pizzas-exist.guard";
export * from "./pizza-toppings.guard";
