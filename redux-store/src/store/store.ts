export class Store {
  private subscribers: Function[];
  private reducers: { [key: string]: Function };
  private state: { [key: string]: any };

  constructor(reducers = {}, initialState = {}) {
    this.subscribers = [];
    this.reducers = reducers;
    this.state = this.reduce(initialState, {});
  }

  get value() {
    return this.state;
  }

  subscribe(fn) {
    this.subscribers = [...this.subscribers, fn];
    this.notify();
    return () => {
      this.subscribers = this.subscribers.filter(x => x != fn);
    };
  }

  dispatch(action) {
    this.state = this.reduce(this.state, action);
    // this applies all the subscriber functions to our state everytime we dispatch an action
    this.notify();
  }

  private notify() {
    this.subscribers.forEach(fn => fn(this.value));
  }

  private reduce(state, action) {
    const newState = {};
    for (const prop in this.reducers) {
      // register the reducers
      newState[prop] = this.reducers[prop](state[prop], action); // result of the reducer call
    }
    return newState;
  }
}
