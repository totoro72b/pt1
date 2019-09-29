import { Store } from "@ngrx/store";
import { CanActivate } from "@angular/router";
import { Injectable } from "@angular/core";
import * as fromStore from "../store";
import { of } from "rxjs/observable/of";
import { Observable } from "rxjs/Observable";
import { filter, take, tap, switchMap, catchError } from "rxjs/operators";

@Injectable()
export class PizzaToppingsGuard implements CanActivate {
  constructor(private store: Store<fromStore.ProductsState>) {}
  canActivate(): Observable<boolean> {
    // NOTE: can activate won't resolve until pizza is successfully loaded or things go wrong
    // in this case it won't return false unless something goes wrong
    return this.checkStore().pipe(
      switchMap(() => of(true)),
      catchError(() => of(false))
    );
  }

  checkStore(): Observable<boolean> {
    // return (finish stream) iff loaded is true via filter
    return this.store.select(fromStore.getToppingsLoaded).pipe(
      tap(loaded => {
        if (!loaded) {
          this.store.dispatch(new fromStore.LoadToppings());
        }
      }),
      filter(loaded => loaded), // filters out all the non-loaded ones -> won't continue until loaded is true
      take(1) // finishes the stream
    );
  }
}
