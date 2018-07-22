import {empty} from 'rxjs/observable/empty';

// empty observable. immediately completes
const src = empty();

src.subscribe({
  next: (x) => console.log('next', x), //no next for empty observable
  complete: () => console.log('complete')
});
