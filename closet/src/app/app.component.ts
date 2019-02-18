import { Component, OnInit } from "@angular/core";
import { FormGroup, FormControl } from "@angular/forms";
import { Item } from "./types";
import { flatMap, debounceTime, distinctUntilChanged } from "rxjs/operators";

const ALL = "all";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.scss"]
})
export class AppComponent implements OnInit {
  title = "closet";
  items: Item[] = null;
  filteredItems: Item[] = [];
  isDropdownOpen = false;
  allCategories: string[] = [];
  searchfg: FormGroup = new FormGroup({
    search: new FormControl(),
    category: new FormControl()
  });

  filterItems(changes: any) {
    const keyword = changes.search || "";
    const category = changes.category === ALL ? "" : changes.category;
    console.log("category is", category);
    console.log("change str", keyword);
    // TODO add debounce
    this.filteredItems = this.items.filter(
      x =>
        x.description.toLowerCase().includes(keyword.toLowerCase()) &&
        x.category.toLowerCase().includes(category)
    );
  }

  toggleCategoryDropdown(): void {
    this.isDropdownOpen = !this.isDropdownOpen;
  }

  setCategory(cat: string): void {
    this.searchfg.get("category").setValue(cat);
    this.toggleCategoryDropdown();
  }

  ngOnInit() {
    this.searchfg.get("category").setValue(ALL);
    this.searchfg.valueChanges
      .pipe(
        debounceTime(500),
        distinctUntilChanged() // FIXME: doesn't really work
      )
      .subscribe(changes => {
        this.filterItems(changes);
      });
    this.items = [
      {
        category: "top",
        description: "fav blouse",
        imgUrl:
          "https://images.anthropologie.com/is/image/Anthropologie/4110084326168_089_b?$an-category$&qlt=80&fit=constrain",
        id: 1
      },
      {
        category: "bottom",
        description: "skirt",
        imgUrl:
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7z09tXLDZODUEJLM5q6neP0NXLBhjckrZz6ZIXOzjBsLCP9NVrw",
        id: 2
      },
      {
        category: "accessory",
        description: "pink hat",
        imgUrl:
          "https://www.acnestudios.com/on/demandware.static/-/Sites-acne-product-catalog/default/dwdfbd534d/images/D4/D40001-/1500x/D40001-418_C.jpg",
        id: 3
      }
    ];
    this.allCategories = this.items.map(x => x.category.toLowerCase());
    this.allCategories.push(ALL);
    this.filteredItems = [...this.items];
  }
}
