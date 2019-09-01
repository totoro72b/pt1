import { Component, OnInit, ChangeDetectionStrategy } from "@angular/core";
import { Store } from "@ngrx/store";
import { Observable } from "rxjs/observable";

import { Pizza } from "../../models/pizza.model";
import { PizzasService } from "../../services/pizzas.service";
import * as fromStore from "../../store";

@Component({
  selector: "products",
  styleUrls: ["products.component.scss"],
  template: `
    <div class="products">
      <div class="products__new">
        <a class="btn btn__ok" routerLink="./new">
          New Pizza
        </a>
      </div>
      <div class="products__list">
        <div *ngIf="!(pizzas$ | async)?.length">
          No pizzas, add one to get started.
        </div>
        <pizza-item *ngFor="let pizza of pizzas$ | async" [pizza]="pizza">
        </pizza-item>
      </div>
    </div>
  `
})
export class ProductsComponent implements OnInit {
  pizzas$: Observable<Pizza[]>;

  // todo does this ask ngrx to inject a store of this type?
  constructor(private store: Store<fromStore.ProductsState>) {}

  ngOnInit() {
    console.log("got store!", this.store);
    // todo what's a memoized selector?
    this.pizzas$ = this.store.select(fromStore.getAllPizzas);
    this.store.dispatch(new fromStore.LoadPizzas(null));
    this.store.dispatch(new fromStore.LoadToppings());
    this.pizzas$.subscribe(x => {
      console.log("get all pizzas", x);
    });
  }
}
