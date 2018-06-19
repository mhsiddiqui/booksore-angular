import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { GridBook } from '../../models/bookstore-models';

@Component({
  selector: 'grid-book',
  templateUrl: './grid-book.component.html',
  styleUrls: ['./grid-book.component.css']
})
export class GridBookComponent implements OnInit {

  @Input() book: GridBook;
  @Output() selected = new EventEmitter();
  button_text = "Add to Cart";

  constructor() { }

  ngOnInit() {
  }

  addToCart(book: GridBook): void {
    this.button_text = "Added";
    this.book.selected = true;
    this.selected.emit(book);
  }

}
