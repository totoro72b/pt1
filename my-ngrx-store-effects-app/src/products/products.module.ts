import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { Routes, RouterModule } from "@angular/router";
import { ReactiveFormsModule } from "@angular/forms";
import { HttpClientModule } from "@angular/common/http";
//ngrx stuff
import { StoreModule } from "@ngrx/store";
import { EffectsModule } from "@ngrx/effects";
import { reducers, effects } from "./store";

// guards
import * as fromGuards from "./guards";

// components
import * as fromComponents from "./components";

// containers
import * as fromContainers from "./containers";

// services
import * as fromServices from "./services";

// routes
export const ROUTES: Routes = [
  {
    path: "",
    canActivate: [fromGuards.PizzasGuard],
    component: fromContainers.ProductsComponent
  },
  {
    path: "new",
    canActivate: [fromGuards.PizzasGuard, fromGuards.PizzaToppingsGuard],
    component: fromContainers.ProductItemComponent
  },
  {
    path: ":pizzaId",
    canActivate: [fromGuards.PizzasExistGuard, fromGuards.PizzaToppingsGuard],
    component: fromContainers.ProductItemComponent
  }
];

@NgModule({
  imports: [
    CommonModule,
    ReactiveFormsModule,
    HttpClientModule,
    RouterModule.forChild(ROUTES),
    //todo is this "registering" reducers?
    // lazy loading products module
    StoreModule.forFeature("products", reducers),
    EffectsModule.forFeature(effects)
  ],
  providers: [...fromServices.services, ...fromGuards.guards],
  declarations: [...fromContainers.containers, ...fromComponents.components],
  exports: [...fromContainers.containers, ...fromComponents.components]
})
export class ProductsModule {}
