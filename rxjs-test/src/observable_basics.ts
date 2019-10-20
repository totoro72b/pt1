import { Observable, Subscriber } from "rxjs";

/*
 * observers can register up to 3 callbacks.
 * next is called 1:M times
 * error is called <= 1 time
 * complete is called <= 1 time
 */
const observer = {
  next: (x: any) => console.log("observer next val:", x),
  error: (err: any) => console.log("observer err val:", err),
  complete: () => console.log("observer complete!")
};
// const observable = Observable.create((subscriber: any) => {
const obs1 = new Observable((subscriber: any) => {
  subscriber.next("hello");
  subscriber.next("world");
  subscriber.error("uh oh");
  // once complete called, observable will be cleaned up and no future values delivered
  subscriber.complete();
  // will not be logged
  subscriber.next("hello 2");
  subscriber.next("world 2");
});

obs1.subscribe(observer);

/** another style : passing in the funcs directly  */
// obs1.subscribe(
//   // next
//   (x: any) => {
//     console.log("obs1 subcribe got ", x);
//   },
//   //error
//   // (x: any) => {
//   //   console.log("err2", x);
//   // },
//   null, // can skip the error func like this
//   //complete
//   () => {
//     console.log("obs1 sub complete");
//   }
// );
