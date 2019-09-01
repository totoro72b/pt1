import { Actions, Effect } from "@ngrx/effects";
import * as pizzasActions from "../actions/pizzas.action";
import * as fromServies from "../../services";
import { switchMap, map, catchError } from "rxjs/operators";
import { of } from "rxjs/observable/of";
import { Injectable } from "@angular/core";
import { effects } from ".";

// basically talks to service and get stuff and then dispatch success/fail actions

@Injectable()
export class PizzasEffects {
  constructor(
    // pizzaAction$: pizzasActions.PizzasAction, // todo what if this???
    private actions$: Actions,
    private pizzaService: fromServies.PizzasService
  ) {}

  // takes effect upon this action
  @Effect()
  loadPizzas$ = this.actions$.ofType(pizzasActions.LOAD_PIZZAS).pipe(
    // switchmap lets us switch to a new observable
    switchMap(() => {
      return this.pizzaService.getPizzas().pipe(
        //todo why only needs of for catcherror case?
        map(pizzas => new pizzasActions.LoadPizzasSuccess(pizzas)),
        catchError(error => of(new pizzasActions.LoadPizzasFail(error)))
      );
    })
  );
  // an effect that listens to the createPizza action
  @Effect()
  createPizza$ = this.actions$.ofType(pizzasActions.CREATE_PIZZA).pipe(
    map((action: pizzasActions.CreatePizza) => action.payload),
    switchMap(pizza => {
      return this.pizzaService.createPizza(pizza).pipe(
        // todo double check map interface (it gets the stuff inside hte observable)
        map(pizza => new pizzasActions.CreatePizzaSuccess(pizza)),
        catchError(error => of(new pizzasActions.CreatePizzaFail(error)))
      );
    })
  );

  @Effect()
  updatePizza$ = this.actions$.ofType(pizzasActions.UPDATE_PIZZA).pipe(
    map((action: pizzasActions.UpdatePizza) => action.payload),
    switchMap(pizza => {
      return this.pizzaService.updatePizza(pizza).pipe(
        map(pizza => new pizzasActions.UpdatePizzaSuccess(pizza)),
        catchError(error => of(new pizzasActions.UpdatePizzaFail(error)))
      );
    })
  );

  @Effect()
  removePizza$ = this.actions$.ofType(pizzasActions.REMOVE_PIZZA).pipe(
    map((action: pizzasActions.RemovePizza) => action.payload),
    switchMap(pizza => {
      return this.pizzaService.removePizza(pizza).pipe(
        // the server won't give us the pizza back
        map(() => new pizzasActions.RemovePizzaSuccess(pizza)),
        catchError(error => of(new pizzasActions.RemovePizzaFail(error)))
      );
    })
  );
}
