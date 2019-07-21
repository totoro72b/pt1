export class Store {
  private subscribers: Function[];
  private reducers: { [key: string]: Function };
  private state: { [key: string]: any };

  constructor(reducers = {}, initialState = {}) {
    this.reducers = reducers;
    this.state = initialState;
  }

  get value() {
    return this.state;
  }
  dispatch(action) {
    // action has payload and type. here we ignore type for now
    // append todos to state
    // this is the job of the reducers. TODO fix it
    // questinos; WHO passes reducers to the store?
    //should store have it? or app?
    // how can store call the reducer w/o konwing anythinga bout it?
    // TODO how to select hte correct reducers?
    this.state = this.reducers[action.type](this.state, action);
  }
}
