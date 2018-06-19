import { Injectable } from '@angular/core';
import {ApiService} from "../api.service";
import { GridBook } from '../../models/bookstore-models'

@Injectable({
  providedIn: 'root'
})
export class BookService {

  getBooks(): any {
    return this.getBooksByUrl('/book_service/book')
  }

  getBooksByUrl(url): any {
    return this.api.call('get', url)
  }

  constructor(private api: ApiService) { }
}
