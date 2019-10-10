import { Observable } from "rxjs";
var obs = Observable.create((observer: any) => {
  observer.next("asdf");
});

obs.subscribe((x: any) => {
  console.log("observer got", x);
});
