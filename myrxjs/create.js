import {Observable} from 'rxjs/Observable';

// Create an observable with given subscription function.
const src = Observable.create((observer)=>{
  console.log('observer type', typeof(observer));
  observer.next('hello');
  observer.next('world');
});

src.subscribe(x=>console.log(x));



/*
 * example 2
  Increment value every 1s, emit even numbers.
*/
const evenNumbers = Observable.create(function(observer) {
  let value = 0;
  const interval = setInterval(() => {
    if (value % 2 === 0) {
      observer.next(value);
    }
    value++;
  }, 1000);

  return () => clearInterval(interval);
});
//output: 0...2...4...6...8
const subscribe = evenNumbers.subscribe(val => console.log('num', val));
//unsubscribe after 10 seconds
setTimeout(() => {
  subscribe.unsubscribe();
}, 10000);
