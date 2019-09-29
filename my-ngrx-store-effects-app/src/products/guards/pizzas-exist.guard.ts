import { Store } from "@ngrx/store";
import { CanActivate, ActivatedRouteSnapshot } from "@angular/router";
import { Injectable } from "@angular/core";
import * as fromStore from "../store";
import { of } from "rxjs/observable/of";
import { Observable } from "rxjs/Observable";
import { filter, take, tap, switchMap, catchError, map } from "rxjs/operators";
import { Pizza } from "../models/pizza.model";

@Injectable()
export class PizzasExistGuard implements CanActivate {
  constructor(private store: Store<fromStore.ProductsState>) {}
  canActivate(route: ActivatedRouteSnapshot): Observable<boolean> {
    // NOTE: can activate won't resolve until pizza is successfully loaded or things go wrong
    // in this case it won't return false unless something goes wrong
    return this.checkStore().pipe(
      switchMap(() => {
        const id = +route.params.pizzaId;
        return this.checkPizzaExists(id);
      }),
      catchError(() => of(false))
    );
  }

  checkPizzaExists(id: number): Observable<boolean> {
    return this.store.select(fromStore.getPizzasEntities).pipe(
      map((pizzaEntities: { [key: number]: Pizza }) => !!pizzaEntities[id]),
      take(1) // TODO necessary?
    );
  }

  checkStore(): Observable<boolean> {
    // return (finish stream) iff loaded is true via filter
    return this.store.select(fromStore.getPizzasLoaded).pipe(
      tap(loaded => {
        if (!loaded) {
          this.store.dispatch(new fromStore.LoadPizzas(null));
        }
      }),
      filter(loaded => loaded), // filters out all the non-loaded ones -> won't continue until loaded is true
      take(1) // finishes the stream
    );
  }
}
