import { of } from "rxjs";
import { distinctUntilKeyChanged, distinctUntilChanged } from "rxjs/operators";

const source1$ = of(1, 2, 3, 3, 3, 2, 3, "3");
// by default triple equal === operator, so we have 3 and '3' in the end
source1$.pipe(distinctUntilChanged()).subscribe(console.log);

// define our own equal function
source1$
  .pipe(distinctUntilChanged((x, y) => x == y))
  .subscribe(x => console.log("custom ", x)); // 3 only printed once at the end

const source2$ = of(
  { name: "asdf", id: 1 },
  { name: "asdf", id: 2 },
  { name: "asdf", id: 3 },
  { name: "asdf new", id: 4 }
);
// shortcut to compare only keys of objects (vs. define custom comparison func in distinctUntilChanged)
source2$.pipe(distinctUntilKeyChanged("name")).subscribe(console.log);
