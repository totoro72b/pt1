import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Item } from './types';
import { flatMap, debounceTime, distinctUntilChanged } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'closet';
  items: Item[] = null;
  filteredItems: Item[] = [];
  searchfg: FormGroup = new FormGroup({
    search: new FormControl(),
    category: new FormControl()
  });

  onSearchChanges(changes: any) {
    const keyword = changes.search;
    console.log('change str', keyword);
    // TODO add debounce
    this.filteredItems = this.items.filter(x =>
      x.description.toLowerCase().includes(keyword.toLowerCase())
    );
  }

  ngOnInit() {
    this.searchfg.valueChanges
      .pipe(
        debounceTime(500),
        distinctUntilChanged() // FIXME: doesn't really work
      )
      .subscribe(changes => {
        this.onSearchChanges(changes);
      });
    this.items = [
      {
        category: 'top',
        description: 'fav blouse',
        imgUrl:
          'https://images.anthropologie.com/is/image/Anthropologie/4110084326168_089_b?$an-category$&qlt=80&fit=constrain',
        id: 1
      },
      {
        category: 'bottom',
        description: 'skirt',
        imgUrl:
          'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7z09tXLDZODUEJLM5q6neP0NXLBhjckrZz6ZIXOzjBsLCP9NVrw',
        id: 2
      },
      {
        category: 'accessory',
        description: 'pink hat',
        imgUrl:
          'https://www.acnestudios.com/on/demandware.static/-/Sites-acne-product-catalog/default/dwdfbd534d/images/D4/D40001-/1500x/D40001-418_C.jpg',
        id: 3
      }
    ];
    this.filteredItems = [...this.items];
  }
}
