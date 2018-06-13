import { Component, OnInit } from '@angular/core';
import { GridBook } from '../../models/bookstore-models';

@Component({
  selector: 'grid-book',
  templateUrl: './grid-book.component.html',
  styleUrls: ['./grid-book.component.css']
})
export class GridBookComponent implements OnInit {

  book: GridBook;

  constructor() { }

  ngOnInit() {
  }

}
