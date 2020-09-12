// catchError!

console.clear();

// begin lesson code
import { empty, fromEvent, of } from "rxjs";
import {
  catchError,
  debounceTime,
  delay,
  switchMap,
  tap
} from "rxjs/operators";

const BASE_URL = "https://api.openbrewerydb.org/breweries";

// streams
const click$ = fromEvent(document, "click");
const fakeRequest$ = (value: any) => of(value.slice(0, 2)).pipe(delay(300));

click$
  .pipe(
    debounceTime(200),
    tap(() => console.log("clicked")),
    switchMap(() =>
      // we are catching the error on the ajax observable returned by switchMap
      // if catchError is put on the click$ stream, it'll complete that stream upon error
      // which prevents it from receving further click events, and we don't wnat that
      fakeRequest$([123]).pipe(
        catchError((error, caught) => {
          console.log("error", error);
          //   return caught;  // NOTE: return caught will cause retry
          return empty();
        })
      )
    )
  )
  .subscribe((response: any) => {
    console.log("got response!", response);
  });
