// an effect is an injectable
import { of } from "rxjs/observable/of";
import { map, catchError, switchMap } from "rxjs/operators";
import { Actions, Effect } from "@ngrx/effects";

import * as toppingsActions from "../actions/toppings.action";
import * as fromServices from "../../services/toppings.service";
import { Injectable } from "@angular/core";

@Injectable() // so we can inject it in the constructor
export class ToppingsEffects {
  constructor(
    private actions$: Actions,
    private toppingsService: fromServices.ToppingsService
  ) {}

  @Effect()
  loadToppings$ = this.actions$.ofType(toppingsActions.LOAD_TOPPINGS).pipe(
    switchMap(() => {
      return this.toppingsService.getToppings().pipe(
        map(toppings => new toppingsActions.LoadToppingsSuccess(toppings)),
        catchError(error => of(new toppingsActions.LoadToppingsFail(error)))
      );
    })
  );
}
