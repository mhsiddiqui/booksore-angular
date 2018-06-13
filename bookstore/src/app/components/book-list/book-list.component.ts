import { Component, OnInit } from '@angular/core';
import { GridBook } from '../../models/bookstore-models'
import { BookService } from '../../service/book/book.service'

@Component({
  selector: 'book-list',
  templateUrl: './book-list.component.html',
  styleUrls: ['./book-list.component.css']
})
export class BookListComponent implements OnInit {

  books: GridBook[];

  constructor(private bookService: BookService) { }

  ngOnInit() {
    this.getBooks();
  }

  getBooks(): void {
    let self = this;
    self.bookService.getBooks().then(function (response) {
      self.books = response;
    })
  }

}
