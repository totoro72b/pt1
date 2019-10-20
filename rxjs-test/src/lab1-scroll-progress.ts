/** lab 1: progres bar */
import { fromEvent } from "rxjs";
import { map } from "rxjs/operators";

function calculateScrollPercent(element: any) {
  // scrollTop: location at the "top of the scroll track"
  // scrollHeight: think of as length of the entire element w/o needing a scrollbar
  // clientHeight: how much of that fits on your screen
  // 100% is at the largest scrollTop position = scrollHeight - clientHeight
  const { scrollTop, scrollHeight, clientHeight } = element;
  console.log("element heights", scrollTop, scrollHeight, clientHeight);
  return (scrollTop / (scrollHeight - clientHeight)) * 100;
}

const progress$ = fromEvent(document, "scroll").pipe(
  map(({ target }: any) => calculateScrollPercent(target.documentElement))
);
progress$.subscribe(console.log);
