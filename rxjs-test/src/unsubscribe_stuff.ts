import { Observable } from "rxjs";

const observer = {
  next: (x: any) => console.log("next", x),
  error: (err: any) => console.log("err", err),
  complete: () => console.log("complete!")
};

const observable = new Observable(subscriber => {
  let c = 0;
  // feed a number to its subscriber every second
  const id = setInterval(() => {
    c += 1;
    subscriber.next(c);
  }, 1000);
  // return a unsubscribe func for the subscriber to call
  const unsubFunc = () => {
    console.log("unsub func called. clear ", id);
    clearInterval(id);
  };
  return unsubFunc;
});

const sub1 = observable.subscribe(observer);
const sub2 = observable.subscribe(observer);
setTimeout(() => {
  sub1.unsubscribe(); // calls the unsubFunc after 3s
}, 3000);

setTimeout(() => {
  sub2.unsubscribe(); // calls the unsubFunc after 5s
}, 5000);
/** NOTE: same definition of observable and observer called twice,
 * we have two different running instances of streams because
 * a new instance of setInterval is instantiated for each, so
 * sub1.unsubscribe() doesn't prevent sub2 from keep going
 */

/** NOTE can unsubscribe both at the same time */
// sub1.add(sub2);
// sub1.unsubscribe()
