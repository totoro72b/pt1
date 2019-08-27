import * as fromRouter from "@ngrx/router-store";
import {
  Params,
  RouterStateSnapshot,
  ActivatedRouteSnapshot
} from "@angular/router";
import { ActionReducerMap, createFeatureSelector } from "@ngrx/store";

// define our own routerState type
export interface RouterStateUrl {
  url: string;
  queryParams: Params;
  params: Params;
}

export interface State {
  myRouterReducer: fromRouter.RouterReducerState<RouterStateUrl>;
}

export const reducers: ActionReducerMap<State> = {
  // so we're using ngrx's router reducer here out of the box
  myRouterReducer: fromRouter.routerReducer
};

// create a feature selector to grab router state
// note the key 'routerReducer' matches the one defined in reducers above
export const getRouterState = createFeatureSelector<
  fromRouter.RouterReducerState<RouterStateUrl>
>("myRouterReducer");

// custom serializer
export class CustomSerializer
  implements fromRouter.RouterStateSerializer<RouterStateUrl> {
  // this function is called whenever the app's route changes
  // it listens to angular's router event
  serialize(routerState: RouterStateSnapshot): RouterStateUrl {
    // const url = routerState.url; V destructuring
    const { url } = routerState;
    const { queryParams } = routerState.root;
    let state: ActivatedRouteSnapshot = routerState.root;
    // loop to the last firstChild
    while (state.firstChild) {
      state = state.firstChild;
    }
    const { params } = state;
    return { url, queryParams, params };
  }
}
