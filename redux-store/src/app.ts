// this pulls everyrting from index.ts, which contains everything from reducers and store so far
import * as fromStore from './store'; // NOTE: this is the store folder, not store.ts
import { renderTodos } from './utils';

const input = document.querySelector('input') as HTMLInputElement;
const button = document.querySelector('button') as HTMLButtonElement;
const destroy = document.querySelector('.unsubscribe') as HTMLButtonElement;
const todoList = document.querySelector('.todos') as HTMLLIElement;

const reducers = {
  todos: fromStore.reducer // this is from store/reducers.ts exported functino reducer
};

// add event listeners
button.addEventListener(
  'click',
  () => {
    if (!input.value.trim()) return;
    const todo = { label: input.value, complete: false };
    // store.dispatch({ type: 'ADD_TODO', payload });
    store.dispatch(new fromStore.AddTodo(todo));
    input.value = '';
  },
  false
);

todoList.addEventListener('click', function(event) {
  const target = event.target as HTMLButtonElement;
  if (target.nodeName.toLowerCase() === 'button') {
    const todo = JSON.parse(target.getAttribute('data-todo') as any);
    store.dispatch(new fromStore.RemoveTodo(todo));
  }
});

const store = new fromStore.Store(reducers);
const action = {
  payload: { label: 'asdf', complete: false },
  type: fromStore.ADD_TODO
};

store.dispatch(action);

const unsubscribeRender = store.subscribe(state => {
  return renderTodos(state.todos.data);
});

// const unsubscribeLog = store.subscribe(state => {
//   console.log('todos are', state.todos.data);
// });

destroy.addEventListener('click', unsubscribeRender, false);

console.log('got store value', store.value);

console.log('from store is', fromStore);
