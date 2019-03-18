export interface Item {
  description: string;
  category: string;
  imgUrl: string;
  id: number;
}

export interface SaveItemEvent {
  item: Item;
  index: number;
}
