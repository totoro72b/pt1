import { PizzasEffects } from "./pizzas.effect";
import { ToppingsEffects } from "./toppings.effect";
// this is used in products.module
export const effects: any[] = [PizzasEffects, ToppingsEffects];
// todo why do we need these exports? shouldn't the above effects be enough?
export * from "./pizzas.effect";
export * from "./toppings.effect";
