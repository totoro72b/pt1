// this pulls everyrting from index.ts, which contains everything from reducers and store so far
import * as fromStore from "./store";
import { renderTodos } from "./utils";

const input = document.querySelector("input") as HTMLInputElement;
const button = document.querySelector("button") as HTMLButtonElement;
const destroy = document.querySelector(".unsubscribe") as HTMLButtonElement;
const todoList = document.querySelector(".todos") as HTMLLIElement;

const reducers = {
  todos: fromStore.reducer
};

// add event listeners
button.addEventListener(
  "click",
  () => {
    if (!input.value.trim()) return;
    const payload = { label: input.value, complete: false };
    store.dispatch({ type: "ADD_TODO", payload });
    console.log(store.value);
    input.value = "haha";
  },
  false
);

todoList.addEventListener("click", function(event) {
  const target = event.target as HTMLButtonElement;
  if (target.nodeName.toLowerCase() === "button") {
    console.log("target", target);
  }
});

const store = new fromStore.Store(reducers);
const action = {
  payload: { label: "asdf", complete: false },
  type: "ADD_TODO"
};
store.dispatch(action);
console.log("got store value", store.value);
