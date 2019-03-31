export interface Item {
  description: string;
  category: string;
  imgUrl: string;
  id: number;
}

export interface SaveItem {
  item: Item;
  index: number;
}
