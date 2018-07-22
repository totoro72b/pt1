import {of} from 'rxjs/observable/of';

const source1 = of(1,2,3,4);
const source2 = of([1,2,3,4]);

source1.subscribe(x=>console.log('src1', x));
source2.subscribe(x=>console.log('src2', x));


// another way to import?
//Rx.Observable.of(11,'haha').subscribe(x=>console.log('import2', x));
