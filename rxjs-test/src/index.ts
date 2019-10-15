import { Observable, Subscriber } from "rxjs";

/*
 * observers can register up to 3 callbacks.
 * next is called 1:M times
 * error is called <= 1 time
 * complete is called <= 1 time
 */
const observer = {
  next: (x: any) => console.log("next val:", x),
  error: (err: any) => console.log("err val:", err),
  complete: () => console.log("complete!")
};
// const observable = Observable.create((subscriber: any) => {
const observable = new Observable((subscriber: any) => {
  subscriber.next("hello");
  subscriber.next("world");
  subscriber.error("uh oh");
  // once complete called, observable will be cleaned up and no future values delivered
  subscriber.complete();
  // will not be logged
  subscriber.next("hello 2");
  subscriber.next("world 2");
});

observable.subscribe(observer);
// another style by passing in the funcs directly
observable.subscribe(
  // next
  (x: any) => {
    console.log("my sub here", x);
  },
  //error
  // (x: any) => {
  //   console.log("err2", x);
  // },
  null, // can skip the error func like this
  //complete
  () => {
    console.log("complete2");
  }
);

// observable with an interval emit thing that can be cancelled
// upon subscriber.complete when you return the func to clearInterval
const obs = new Observable(subscriber => {
  let count = 0;
  const id = setInterval(() => {
    subscriber.next(count);
    console.log("id is", id); // id stays the same
    subscriber.complete();
    count += 1;
  }, 500);

  // called upon subscriber complete.
  // w/o clearInterval, the interval keeps emitting even after subscriber.complete() is called
  return () => {
    console.log("return func called");
    clearInterval(id);
  };
});

console.log("before");
obs.subscribe(observer);
console.log("after");
