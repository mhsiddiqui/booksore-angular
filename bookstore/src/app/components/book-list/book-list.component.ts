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
  next: string = "";
  previous: string = "";

  constructor(private bookService: BookService) { }

  ngOnInit() {
    this.getBooks();
  }

  getBooks(): void {
    let self = this;
    self.bookService.getBooks().then(function (response) {
      self.next = response.next;
      self.previous = response.previous;
      self.books = response.results;
    })
  }

  getBooksByUrl(url): void {
    let self = this;
    self.bookService.getBooksByUrl(url).then(function (response) {
      self.next = response.next;
      self.previous = response.previous;
      self.books = response.results;
    })
  }

  method(event): void {
    console.log(event);
  }

}
