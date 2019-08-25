import { Actions, Effect } from "@ngrx/effects";
import * as pizzasActions from "../actions/pizzas.action";
import * as fromServies from "../../services";
import { switchMap, map, catchError } from "rxjs/operators";
import { of } from "rxjs/observable/of";
import { Injectable } from "@angular/core";

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
}
