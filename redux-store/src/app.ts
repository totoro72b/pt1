import * as fromStore from "./store/store";
import reducers from "./store/reducers";
import { renderTodos } from "./utils";

const input = document.querySelector("input") as HTMLInputElement;
const button = document.querySelector("button") as HTMLButtonElement;
const destroy = document.querySelector(".unsubscribe") as HTMLButtonElement;
const todoList = document.querySelector(".todos") as HTMLLIElement;

// add event listeners
button.addEventListener(
  "click",
  () => {
    if (!input.value.trim()) return;
    console.log("document is", document);

    const payload = { label: input.value, complete: false };

    console.log("payload", payload);

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

const store = new fromStore.Store({});
const action = {
  payload: { label: "asdf", complete: false },
  type: "ADD_TODO"
};
store.dispatch(action);
console.log("got store value", store.value);
